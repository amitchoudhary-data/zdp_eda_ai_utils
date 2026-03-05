#!/usr/bin/env python3
"""
COLUMN LEVEL MODEL ANALYSIS AGENT

Analyzes a DBT model to find all source references for specified columns/fields.
Identifies alias names and provides structured output in gsheets-compatible format.

Usage:
    python3 column_level_model_analyzer.py --model <model_name> --columns <col1,col2,col3>
    python3 column_level_model_analyzer.py --model dim_accounts --columns "instance_account_derived_type,instance_account_is_sandbox"

Author: EDA Team
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass, field


@dataclass
class ColumnReference:
    """Represents a column reference found in a model."""
    column_name: str
    source_table: str
    source_column: str  # Original column name if alias used
    alias_used: bool = False
    context: str = ""  # e.g., "direct", "coalesce", "case_when", "join"
    line_number: int = 0


@dataclass
class AnalysisResult:
    """Complete analysis result for a model."""
    model_name: str
    model_path: str
    columns_analyzed: List[str]
    references: List[ColumnReference] = field(default_factory=list)
    observations: List[str] = field(default_factory=list)


class ColumnLevelModelAnalyzer:
    """
    Agent for analyzing column-level source references in DBT models.
    """
    
    # Common DBT repositories to search
    DEFAULT_REPOS = [
        "zdp_dbt_finance",
        "zdp_dbt_customer", 
        "zdp_dbt_regional_product_analytics",
        "zdp_cloud_dbt_eda_sales_marketing"
    ]
    
    def __init__(self, workspace_path: str = None):
        """Initialize the analyzer with workspace path."""
        self.workspace_path = workspace_path or os.getcwd()
        # Go up to find the repos root if we're in a subdirectory
        if "zdp_eda_ai_utils" in self.workspace_path:
            self.workspace_path = str(Path(self.workspace_path).parent.parent)
        
        self.model_cache: Dict[str, str] = {}
        self.source_definitions: Dict[str, Dict] = {}
        
    def find_model_file(self, model_name: str) -> Optional[str]:
        """Find the SQL file for a given model name."""
        # Remove .sql extension if provided
        model_name = model_name.replace('.sql', '')
        
        # Search across all repos
        for repo in self.DEFAULT_REPOS:
            repo_path = os.path.join(self.workspace_path, repo)
            if not os.path.exists(repo_path):
                continue
                
            # Walk through the repo looking for the model
            for root, dirs, files in os.walk(repo_path):
                # Skip non-model directories
                if 'target' in root or 'dbt_packages' in root or 'logs' in root:
                    continue
                    
                for file in files:
                    if file.endswith('.sql'):
                        file_model_name = file.replace('.sql', '')
                        if file_model_name.lower() == model_name.lower():
                            return os.path.join(root, file)
        
        return None
    
    def read_model_content(self, model_path: str) -> str:
        """Read the content of a model file."""
        try:
            with open(model_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading model file: {e}")
            return ""
    
    def extract_source_references(self, content: str) -> List[Tuple[str, str]]:
        """Extract all source() and ref() references from model content."""
        sources = []
        
        # Pattern for {{ source('schema', 'table') }}
        source_pattern = r"\{\{\s*source\s*\(\s*['\"](\w+)['\"]\s*,\s*['\"](\w+)['\"]\s*\)\s*\}\}"
        for match in re.finditer(source_pattern, content, re.IGNORECASE):
            sources.append(('source', f"{match.group(1)}.{match.group(2)}"))
        
        # Pattern for {{ ref('model_name') }}
        ref_pattern = r"\{\{\s*ref\s*\(\s*['\"](\w+)['\"]\s*\)\s*\}\}"
        for match in re.finditer(ref_pattern, content, re.IGNORECASE):
            sources.append(('ref', match.group(1)))
        
        return sources
    
    def extract_cte_definitions(self, content: str) -> Dict[str, str]:
        """Extract CTE definitions from the model."""
        ctes = {}
        
        # Pattern for CTEs: cte_name as (...)
        # This is a simplified pattern - real CTEs can be complex
        cte_pattern = r'(\w+)\s+as\s*\(\s*(select.*?)(?=\)\s*,\s*\w+\s+as\s*\(|\)\s*select|\)\s*$)'
        
        # Alternative simpler pattern
        simple_cte_pattern = r'(\w+)\s+as\s*\('
        
        matches = list(re.finditer(simple_cte_pattern, content, re.IGNORECASE | re.MULTILINE))
        
        for i, match in enumerate(matches):
            cte_name = match.group(1).lower()
            start_pos = match.end()
            
            # Find the matching closing parenthesis
            paren_count = 1
            end_pos = start_pos
            while end_pos < len(content) and paren_count > 0:
                if content[end_pos] == '(':
                    paren_count += 1
                elif content[end_pos] == ')':
                    paren_count -= 1
                end_pos += 1
            
            cte_content = content[start_pos:end_pos-1]
            ctes[cte_name] = cte_content
        
        return ctes
    
    def find_column_in_content(self, column: str, content: str, source_alias: str = None) -> List[ColumnReference]:
        """Find references to a column in SQL content."""
        references = []
        column_lower = column.lower()
        
        lines = content.split('\n')
        
        for line_num, line in enumerate(lines, 1):
            line_lower = line.lower()
            
            # Skip comments
            if line.strip().startswith('--') or line.strip().startswith('/*'):
                continue
            
            # Check for direct column reference
            # Patterns: column_name, alias.column_name, column_name as alias
            patterns = [
                # column as alias (alias is the output name)
                rf'(\w+)\.?(\w*)\s+as\s+{column_lower}\b',
                # direct reference: table.column or just column
                rf'(\w+)\.{column_lower}\b',
                rf'\b{column_lower}\b',
            ]
            
            for pattern in patterns:
                matches = re.finditer(pattern, line_lower)
                for match in matches:
                    # Determine source table and original column
                    full_match = match.group(0)
                    
                    # Check if this is an alias definition
                    alias_pattern = rf'(\w+)\.(\w+)\s+as\s+{column_lower}'
                    alias_match = re.search(alias_pattern, line_lower)
                    
                    if alias_match:
                        source_table = alias_match.group(1)
                        source_column = alias_match.group(2)
                        ref = ColumnReference(
                            column_name=column,
                            source_table=source_table,
                            source_column=source_column,
                            alias_used=True,
                            context="alias",
                            line_number=line_num
                        )
                        references.append(ref)
                    elif '.' in full_match:
                        # table.column format
                        parts = full_match.split('.')
                        if len(parts) >= 2:
                            table = parts[0].strip()
                            col = parts[1].split()[0].strip()  # Remove any trailing keywords
                            ref = ColumnReference(
                                column_name=column,
                                source_table=table,
                                source_column=col if col != column_lower else column,
                                alias_used=(col != column_lower),
                                context="direct",
                                line_number=line_num
                            )
                            if not any(r.source_table == ref.source_table and r.source_column == ref.source_column for r in references):
                                references.append(ref)
        
        # Check for COALESCE patterns
        coalesce_pattern = rf'coalesce\s*\([^)]*{column_lower}[^)]*\)'
        for match in re.finditer(coalesce_pattern, content.lower()):
            coalesce_content = match.group(0)
            # Extract table.column patterns from coalesce
            table_col_pattern = r'(\w+)\.(\w+)'
            for tc_match in re.finditer(table_col_pattern, coalesce_content):
                table = tc_match.group(1)
                col = tc_match.group(2)
                ref = ColumnReference(
                    column_name=column,
                    source_table=table,
                    source_column=col,
                    alias_used=(col != column_lower),
                    context="coalesce",
                    line_number=0
                )
                if not any(r.source_table == ref.source_table and r.source_column == ref.source_column and r.context == "coalesce" for r in references):
                    references.append(ref)
        
        # Check for CASE WHEN patterns
        case_pattern = rf'case\s+when[^)]*{column_lower}[^)]*end'
        for match in re.finditer(case_pattern, content.lower(), re.DOTALL):
            case_content = match.group(0)
            table_col_pattern = r'(\w+)\.(\w+)'
            for tc_match in re.finditer(table_col_pattern, case_content):
                table = tc_match.group(1)
                col = tc_match.group(2)
                if column_lower in col or col in column_lower:
                    ref = ColumnReference(
                        column_name=column,
                        source_table=table,
                        source_column=col,
                        alias_used=(col != column_lower),
                        context="case_when",
                        line_number=0
                    )
                    if not any(r.source_table == ref.source_table and r.source_column == ref.source_column and r.context == "case_when" for r in references):
                        references.append(ref)
        
        return references
    
    def resolve_cte_to_source(self, cte_name: str, ctes: Dict[str, str], column: str, depth: int = 0) -> List[ColumnReference]:
        """Recursively resolve CTE references to find ultimate source."""
        if depth > 10:  # Prevent infinite recursion
            return []
        
        if cte_name.lower() not in ctes:
            return []
        
        cte_content = ctes[cte_name.lower()]
        refs = self.find_column_in_content(column, cte_content)
        
        resolved_refs = []
        for ref in refs:
            # Check if source_table is another CTE
            if ref.source_table.lower() in ctes:
                # Recursively resolve
                deeper_refs = self.resolve_cte_to_source(ref.source_table, ctes, ref.source_column, depth + 1)
                if deeper_refs:
                    resolved_refs.extend(deeper_refs)
                else:
                    resolved_refs.append(ref)
            else:
                resolved_refs.append(ref)
        
        return resolved_refs
    
    def analyze_model(self, model_name: str, columns: List[str]) -> AnalysisResult:
        """
        Main analysis method. Analyzes a model for specified columns.
        """
        result = AnalysisResult(
            model_name=model_name,
            model_path="",
            columns_analyzed=columns
        )
        
        # Find the model file
        model_path = self.find_model_file(model_name)
        if not model_path:
            result.observations.append(f"ERROR: Model '{model_name}' not found in workspace")
            return result
        
        result.model_path = model_path
        result.observations.append(f"Model found at: {model_path}")
        
        # Read model content
        content = self.read_model_content(model_path)
        if not content:
            result.observations.append("ERROR: Could not read model content")
            return result
        
        # Extract source references
        sources = self.extract_source_references(content)
        if sources:
            result.observations.append(f"Sources referenced: {[s[1] for s in sources]}")
        
        # Extract CTEs
        ctes = self.extract_cte_definitions(content)
        if ctes:
            result.observations.append(f"CTEs found: {list(ctes.keys())}")
        
        # Analyze each column
        for column in columns:
            column = column.strip()
            refs = self.find_column_in_content(column, content)
            
            # Resolve CTE references
            resolved_refs = []
            for ref in refs:
                if ref.source_table.lower() in ctes:
                    # Resolve through CTE
                    cte_refs = self.resolve_cte_to_source(ref.source_table, ctes, ref.source_column)
                    if cte_refs:
                        for cte_ref in cte_refs:
                            cte_ref.column_name = column  # Keep original column name
                            resolved_refs.append(cte_ref)
                    else:
                        resolved_refs.append(ref)
                else:
                    resolved_refs.append(ref)
            
            if resolved_refs:
                result.references.extend(resolved_refs)
            else:
                # Column not found - add observation
                result.observations.append(f"Column '{column}' not found with explicit source reference")
                # Add placeholder reference
                result.references.append(ColumnReference(
                    column_name=column,
                    source_table="NOT_FOUND",
                    source_column=column,
                    alias_used=False,
                    context="not_found"
                ))
        
        return result
    
    def format_gsheets_output(self, result: AnalysisResult) -> str:
        """Format the analysis result as tab-separated values for Google Sheets."""
        output_lines = []
        
        # Header
        output_lines.append("Column/Field\tSource Table\tColumn Name in source (if alias used)")
        
        # Maintain column order from input
        column_order = {col.strip(): i for i, col in enumerate(result.columns_analyzed)}
        
        # Sort references by input column order
        sorted_refs = sorted(result.references, key=lambda r: column_order.get(r.column_name, 999))
        
        # Output rows
        for ref in sorted_refs:
            source_col = ref.source_column if ref.alias_used else "-"
            output_lines.append(f"{ref.column_name}\t{ref.source_table}\t{source_col}")
        
        return '\n'.join(output_lines)
    
    def format_markdown_output(self, result: AnalysisResult) -> str:
        """Format the analysis result as Markdown table."""
        output_lines = []
        
        output_lines.append(f"## Column Level Analysis: {result.model_name}")
        output_lines.append("")
        output_lines.append(f"**Model Path:** `{result.model_path}`")
        output_lines.append("")
        
        # Table header
        output_lines.append("| Column/Field | Source Table | Column Name in source (if alias used) |")
        output_lines.append("|:-------------|:-------------|:--------------------------------------|")
        
        # Maintain column order from input
        column_order = {col.strip(): i for i, col in enumerate(result.columns_analyzed)}
        
        # Sort references by input column order
        sorted_refs = sorted(result.references, key=lambda r: column_order.get(r.column_name, 999))
        
        # Output rows
        for ref in sorted_refs:
            source_col = ref.source_column if ref.alias_used else "-"
            output_lines.append(f"| {ref.column_name} | {ref.source_table} | {source_col} |")
        
        # Observations
        if result.observations:
            output_lines.append("")
            output_lines.append("### Observations/Assumptions")
            output_lines.append("")
            for obs in result.observations:
                output_lines.append(f"- {obs}")
        
        return '\n'.join(output_lines)


def main():
    parser = argparse.ArgumentParser(
        description="Column Level Model Analysis Agent for DBT",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python3 column_level_model_analyzer.py --model dim_accounts --columns "col1,col2"
    python3 column_level_model_analyzer.py --model stg_zuora_subscription --columns "subscription_model_type,is_price_ramp"
        """
    )
    
    parser.add_argument(
        '--model',
        required=True,
        help='Name of the DBT model to analyze (without .sql extension)'
    )
    
    parser.add_argument(
        '--columns',
        required=True,
        help='Comma-separated list of columns to analyze'
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
    
    args = parser.parse_args()
    
    # Parse columns
    columns = [c.strip() for c in args.columns.split(',')]
    
    print(f"\n🔍 COLUMN LEVEL MODEL ANALYSIS AGENT")
    print(f"{'='*50}")
    print(f"Model: {args.model}")
    print(f"Columns: {columns}")
    print(f"{'='*50}\n")
    
    # Initialize analyzer
    analyzer = ColumnLevelModelAnalyzer(args.workspace)
    
    # Run analysis
    result = analyzer.analyze_model(args.model, columns)
    
    # Format output
    output_parts = []
    
    if args.format in ['gsheets', 'both']:
        output_parts.append("### Google Sheets Format (Tab-separated)")
        output_parts.append("```")
        output_parts.append(analyzer.format_gsheets_output(result))
        output_parts.append("```")
        output_parts.append("")
    
    if args.format in ['markdown', 'both']:
        output_parts.append(analyzer.format_markdown_output(result))
    
    output = '\n'.join(output_parts)
    
    if args.output:
        with open(args.output, 'w') as f:
            f.write(output)
        print(f"✅ Output saved to: {args.output}")
    else:
        print(output)
    
    print(f"\n{'='*50}")
    print("✅ Analysis complete!")


if __name__ == "__main__":
    main()





