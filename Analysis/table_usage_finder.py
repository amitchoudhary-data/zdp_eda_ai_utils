#!/usr/bin/env python3
"""
TABLE USAGE FINDER AGENT

Analyzes the usage of specific database tables and their columns across a multi-project dbt workspace.
Traces lineage from source table through downstream models to final leaf nodes.

Capabilities:
1. Reference Search: Locate all dbt models that reference a given source table or upstream model
2. Column Usage Analysis: Determine which columns from the source are used (explicit, wildcard, logic)
3. Lineage Tracing: Trace data flow from source to final models

Usage:
    python3 table_usage_finder.py --table <table_name>
    python3 table_usage_finder.py --table <table_name> --columns <col1,col2>
    python3 table_usage_finder.py --table CLEANSED.SALESFORCE.SALESFORCE_LEAD_BCV --columns "id,email"

Author: EDA Team
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple, Optional
from dataclasses import dataclass, field
from collections import defaultdict


@dataclass
class ColumnUsage:
    """Represents how a column is used in a model."""
    column_name: str
    usage_type: str  # 'explicit', 'wildcard', 'where', 'join', 'group_by', 'order_by'
    line_number: int = 0
    context: str = ""


@dataclass
class ModelReference:
    """Represents a model that references a source table."""
    model_name: str
    model_path: str
    repository: str
    reference_type: str  # 'source', 'ref', 'direct'
    columns_used: List[ColumnUsage] = field(default_factory=list)
    uses_wildcard: bool = False
    downstream_models: List[str] = field(default_factory=list)


@dataclass
class LineageEntry:
    """Represents a lineage path for a column."""
    column_name: str
    source_model: str
    used_in_model: str
    repository: str
    lineage_path: str


class TableUsageFinder:
    """
    Agent for finding table usage across multiple dbt repositories.
    """
    
    # DBT repositories to search
    DEFAULT_REPOS = [
        "zdp_dbt_finance",
        "zdp_dbt_customer",
        "zdp_dbt_regional_product_analytics",
        "zdp_cloud_dbt_eda_sales_marketing"
    ]
    
    def __init__(self, workspace_path: str = None):
        """Initialize the finder with workspace path."""
        self.workspace_path = workspace_path or os.getcwd()
        # Go up to find the repos root if we're in a subdirectory
        if "zdp_eda_ai_utils" in self.workspace_path:
            self.workspace_path = str(Path(self.workspace_path).parent.parent)
        
        self.model_index: Dict[str, str] = {}  # model_name -> file_path
        self.ref_graph: Dict[str, Set[str]] = defaultdict(set)  # model -> downstream models
        self._build_model_index()
    
    def _build_model_index(self):
        """Build an index of all models in the workspace."""
        for repo in self.DEFAULT_REPOS:
            repo_path = os.path.join(self.workspace_path, repo)
            if not os.path.exists(repo_path):
                continue
            
            for root, dirs, files in os.walk(repo_path):
                # Skip non-model directories
                if 'target' in root or 'dbt_packages' in root or 'logs' in root:
                    continue
                
                for file in files:
                    if file.endswith('.sql') and 'models' in root:
                        model_name = file.replace('.sql', '')
                        full_path = os.path.join(root, file)
                        self.model_index[model_name.lower()] = full_path
    
    def _get_repository_name(self, file_path: str) -> str:
        """Extract repository name from file path."""
        for repo in self.DEFAULT_REPOS:
            if repo in file_path:
                return repo
        return "unknown"
    
    def _normalize_table_name(self, table_name: str) -> str:
        """Normalize table name for matching."""
        # Handle fully qualified names like CLEANSED.SALESFORCE.TABLE_NAME
        parts = table_name.upper().replace('"', '').replace("'", "").split('.')
        return parts[-1] if parts else table_name.upper()
    
    def find_references(self, table_name: str) -> List[ModelReference]:
        """
        Find all models that reference the given table.
        Searches for source(), ref(), and direct table references.
        """
        references = []
        normalized_name = self._normalize_table_name(table_name)
        
        # Patterns to search for
        patterns = [
            # source('schema', 'table')
            rf"source\s*\(\s*['\"]?\w+['\"]?\s*,\s*['\"]?{normalized_name}['\"]?\s*\)",
            # ref('model')
            rf"ref\s*\(\s*['\"]?{normalized_name}['\"]?\s*\)",
            # Direct table reference
            rf"\b{normalized_name}\b",
        ]
        
        for repo in self.DEFAULT_REPOS:
            repo_path = os.path.join(self.workspace_path, repo)
            if not os.path.exists(repo_path):
                continue
            
            # Search through all SQL files in models directory
            for root, dirs, files in os.walk(repo_path):
                if 'target' in root or 'dbt_packages' in root or 'logs' in root:
                    continue
                if 'models' not in root:
                    continue
                
                for file in files:
                    if not file.endswith('.sql'):
                        continue
                    
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                    except Exception:
                        continue
                    
                    # Check each pattern
                    for i, pattern in enumerate(patterns):
                        if re.search(pattern, content, re.IGNORECASE):
                            model_name = file.replace('.sql', '')
                            ref_type = ['source', 'ref', 'direct'][i]
                            
                            # Check if we already have this reference
                            existing = next((r for r in references if r.model_name == model_name), None)
                            if not existing:
                                ref = ModelReference(
                                    model_name=model_name,
                                    model_path=file_path,
                                    repository=repo,
                                    reference_type=ref_type
                                )
                                
                                # Analyze column usage
                                ref.columns_used, ref.uses_wildcard = self._analyze_column_usage(content, table_name)
                                
                                references.append(ref)
                            break  # Found a match, no need to check other patterns
        
        return references
    
    def _analyze_column_usage(self, content: str, table_name: str) -> Tuple[List[ColumnUsage], bool]:
        """
        Analyze how columns are used in the model content.
        Returns (list of column usages, uses_wildcard flag)
        """
        columns = []
        uses_wildcard = False
        
        # Remove comments
        content_clean = re.sub(r'--.*$', '', content, flags=re.MULTILINE)
        content_clean = re.sub(r'/\*.*?\*/', '', content_clean, flags=re.DOTALL)
        
        normalized_name = self._normalize_table_name(table_name)
        
        # Find alias for the table
        alias_pattern = rf"(?:from|join)\s+.*?{normalized_name}.*?\s+(?:as\s+)?(\w+)"
        alias_match = re.search(alias_pattern, content_clean, re.IGNORECASE | re.DOTALL)
        table_alias = alias_match.group(1) if alias_match else None
        
        # Check for SELECT *
        wildcard_pattern = rf"\bselect\s+(?:\w+\.)?\*"
        if re.search(wildcard_pattern, content_clean, re.IGNORECASE):
            uses_wildcard = True
            columns.append(ColumnUsage(
                column_name="*",
                usage_type="wildcard",
                context="All columns passed through"
            ))
        
        # Find explicit column selections
        # Pattern: table.column or alias.column
        if table_alias:
            col_pattern = rf"\b{table_alias}\.(\w+)\b"
        else:
            col_pattern = rf"\b{normalized_name}\.(\w+)\b"
        
        for match in re.finditer(col_pattern, content_clean, re.IGNORECASE):
            col_name = match.group(1)
            # Determine usage type based on context
            line_start = content_clean.rfind('\n', 0, match.start()) + 1
            line_end = content_clean.find('\n', match.end())
            line = content_clean[line_start:line_end].lower()
            
            if 'where' in line or 'and ' in line or 'or ' in line:
                usage_type = 'where'
            elif 'join' in line or ' on ' in line:
                usage_type = 'join'
            elif 'group by' in line:
                usage_type = 'group_by'
            elif 'order by' in line:
                usage_type = 'order_by'
            else:
                usage_type = 'explicit'
            
            # Avoid duplicates
            if not any(c.column_name.lower() == col_name.lower() and c.usage_type == usage_type for c in columns):
                columns.append(ColumnUsage(
                    column_name=col_name,
                    usage_type=usage_type
                ))
        
        return columns, uses_wildcard
    
    def find_downstream_models(self, model_name: str, visited: Set[str] = None, depth: int = 0) -> List[str]:
        """
        Find all downstream models that reference this model.
        Returns list of downstream model names.
        """
        if visited is None:
            visited = set()
        
        if depth > 10 or model_name.lower() in visited:
            return []
        
        visited.add(model_name.lower())
        downstream = []
        
        # Search for ref('model_name') in all models
        ref_pattern = rf"ref\s*\(\s*['\"]?{model_name}['\"]?\s*\)"
        
        for other_model, path in self.model_index.items():
            if other_model in visited:
                continue
            
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
            except Exception:
                continue
            
            if re.search(ref_pattern, content, re.IGNORECASE):
                downstream.append(other_model)
                # Recursively find further downstream
                further_downstream = self.find_downstream_models(other_model, visited.copy(), depth + 1)
                downstream.extend(further_downstream)
        
        return downstream
    
    def build_lineage(self, table_name: str, columns: List[str] = None) -> List[LineageEntry]:
        """
        Build complete lineage entries for the table and specified columns.
        """
        entries = []
        
        # Find direct references
        references = self.find_references(table_name)
        
        for ref in references:
            # Find downstream models for this reference
            downstream = self.find_downstream_models(ref.model_name)
            ref.downstream_models = downstream
            
            # Determine columns to report
            if columns:
                # Filter to requested columns
                relevant_cols = [c for c in ref.columns_used if c.column_name in columns or c.column_name == '*']
            else:
                relevant_cols = ref.columns_used if ref.columns_used else [ColumnUsage(column_name="*", usage_type="all")]
            
            # Build lineage path
            if downstream:
                lineage_path = f"{ref.model_name} > " + " > ".join(downstream[:5])  # Limit depth
                if len(downstream) > 5:
                    lineage_path += " > ..."
            else:
                lineage_path = ref.model_name
            
            for col in relevant_cols:
                entry = LineageEntry(
                    column_name=col.column_name,
                    source_model=self._normalize_table_name(table_name),
                    used_in_model=ref.model_name,
                    repository=ref.repository,
                    lineage_path=lineage_path
                )
                entries.append(entry)
        
        return entries
    
    def format_markdown_output(self, entries: List[LineageEntry], table_name: str, columns: List[str] = None) -> str:
        """Format output as Markdown table."""
        lines = []
        
        lines.append(f"## Table Usage Analysis: {table_name}")
        lines.append("")
        if columns:
            lines.append(f"**Columns Analyzed:** {', '.join(columns)}")
        else:
            lines.append("**Columns Analyzed:** All columns")
        lines.append("")
        
        # Table header
        lines.append("| Column Name | Source Model | Used in model | Repository Name | Lineage till all downstream models |")
        lines.append("|:------------|:-------------|:--------------|:----------------|:-----------------------------------|")
        
        # Sort entries by column name
        if columns:
            # Maintain input order
            col_order = {c: i for i, c in enumerate(columns)}
            entries = sorted(entries, key=lambda e: col_order.get(e.column_name, 999))
        
        # Remove duplicates while preserving order
        seen = set()
        unique_entries = []
        for entry in entries:
            key = (entry.column_name, entry.used_in_model)
            if key not in seen:
                seen.add(key)
                unique_entries.append(entry)
        
        for entry in unique_entries:
            lines.append(f"| {entry.column_name} | {entry.source_model} | {entry.used_in_model} | {entry.repository} | {entry.lineage_path} |")
        
        if not unique_entries:
            lines.append("| - | - | No references found | - | - |")
        
        return '\n'.join(lines)
    
    def format_gsheets_output(self, entries: List[LineageEntry]) -> str:
        """Format output for Google Sheets (tab-separated)."""
        lines = []
        
        lines.append("Column Name\tSource Model\tUsed in model\tRepository Name\tLineage till all downstream models")
        
        seen = set()
        for entry in entries:
            key = (entry.column_name, entry.used_in_model)
            if key not in seen:
                seen.add(key)
                lines.append(f"{entry.column_name}\t{entry.source_model}\t{entry.used_in_model}\t{entry.repository}\t{entry.lineage_path}")
        
        return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Table Usage Finder Agent for DBT",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 table_usage_finder.py --table salesforce_lead_bcv
    python3 table_usage_finder.py --table CLEANSED.SALESFORCE.SALESFORCE_LEAD_BCV --columns "id,email"
    python3 table_usage_finder.py --table zuora_subscription --columns "subscription_model_type,is_price_ramp"
        """
    )
    
    parser.add_argument(
        '--table',
        required=True,
        help='Name of the table to analyze (can be fully qualified or just table name)'
    )
    
    parser.add_argument(
        '--columns',
        default=None,
        help='Comma-separated list of columns to track (optional, default: all columns)'
    )
    
    parser.add_argument(
        '--workspace',
        default=None,
        help='Path to workspace root (default: current directory)'
    )
    
    parser.add_argument(
        '--format',
        choices=['gsheets', 'markdown', 'both'],
        default='both',
        help='Output format (default: both)'
    )
    
    parser.add_argument(
        '--output',
        default=None,
        help='Output file path (default: print to stdout)'
    )
    
    parser.add_argument(
        '--max-depth',
        type=int,
        default=5,
        help='Maximum depth for lineage tracing (default: 5)'
    )
    
    args = parser.parse_args()
    
    # Parse columns if provided
    columns = [c.strip() for c in args.columns.split(',')] if args.columns else None
    
    print(f"\n🔍 TABLE USAGE FINDER AGENT")
    print(f"{'='*60}")
    print(f"Table: {args.table}")
    print(f"Columns: {columns if columns else 'All columns'}")
    print(f"{'='*60}\n")
    
    # Initialize finder
    finder = TableUsageFinder(args.workspace)
    
    print(f"📊 Indexed {len(finder.model_index)} models across repositories")
    print(f"🔎 Searching for references...\n")
    
    # Build lineage
    entries = finder.build_lineage(args.table, columns)
    
    print(f"✅ Found {len(entries)} column references\n")
    
    # Format output
    output_parts = []
    
    if args.format in ['gsheets', 'both']:
        output_parts.append("### Google Sheets Format (Tab-separated)")
        output_parts.append("```")
        output_parts.append(finder.format_gsheets_output(entries))
        output_parts.append("```")
        output_parts.append("")
    
    if args.format in ['markdown', 'both']:
        output_parts.append(finder.format_markdown_output(entries, args.table, columns))
    
    output = '\n'.join(output_parts)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Output saved to: {args.output}")
    else:
        print(output)
    
    print(f"\n{'='*60}")
    print("✅ Analysis complete!")


if __name__ == "__main__":
    main()





