#!/usr/bin/env python3
"""
SFDC Field Analysis Helper - Local Multi-Repo Version
Generates structured analysis requests for Claude across multiple local repositories

Usage:
    python sfdc_field_analyzer_local.py --fields="field1,field2,field3" --repo-config="repos.json"
    python sfdc_field_analyzer_local.py --fields="field1,field2,field3" --repo-paths="/path/repo1,/path/repo2"
"""

import argparse
import json
import os
from datetime import datetime
from typing import List, Dict
from pathlib import Path

def load_repo_config(config_file: str) -> Dict[str, str]:
    """Load repository configuration from JSON file"""
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config.get('repositories', {})
    except FileNotFoundError:
        print(f"⚠️  Config file {config_file} not found. Creating example...")
        create_example_config(config_file)
        return {}
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in {config_file}")
        return {}

def create_example_config(config_file: str):
    """Create an example repository configuration file"""
    example_config = {
        "repositories": {
            "zdp_dbt_finance": {
                "path": "/path/to/zdp_dbt_finance",
                "type": "dbt",
                "priority": "high",
                "description": "Finance data models and metrics"
            },
            "zdp_dbt_core": {
                "path": "/path/to/zdp_dbt_core", 
                "type": "dbt",
                "priority": "high",
                "description": "Core data models and shared components"
            },
            "zdp_dbt_marketing": {
                "path": "/path/to/zdp_dbt_marketing",
                "type": "dbt", 
                "priority": "medium",
                "description": "Marketing analytics and attribution"
            },
            "airflow_dags": {
                "path": "/path/to/airflow_dags",
                "type": "airflow",
                "priority": "low",
                "description": "Data pipeline orchestration"
            }
        },
        "analysis_settings": {
            "focus_areas": [
                "Price ramp identification logic",
                "Revenue recognition calculations", 
                "SFA quarterly analysis models",
                "MBA reporting dependencies",
                "Digital-led renewal logic"
            ],
            "search_paths": {
                "staging": ["src/models/staging/", "models/staging/", "staging/"],
                "foundational": ["src/models/foundational/", "models/foundational/", "foundational/"],
                "functional": ["src/models/functional/", "models/functional/", "functional/"]
            }
        }
    }
    
    with open(config_file, 'w') as f:
        json.dump(example_config, f, indent=2)
    
    print(f"📄 Example config created: {config_file}")
    print("   Please update the repository paths and run again.")

def validate_repositories(repo_config: Dict[str, Dict]) -> Dict[str, Dict]:
    """Validate that repository paths exist and are accessible"""
    valid_repos = {}
    
    for repo_name, repo_info in repo_config.items():
        repo_path = repo_info.get('path', '')
        
        if os.path.exists(repo_path):
            valid_repos[repo_name] = repo_info
            print(f"✅ {repo_name}: {repo_path}")
        else:
            print(f"❌ {repo_name}: Path not found - {repo_path}")
    
    return valid_repos

def generate_multi_repo_claude_prompt(field_names: List[str], repo_config: Dict[str, Dict]) -> str:
    """Generate Claude analysis prompt for multiple repositories"""
    
    repo_list = list(repo_config.keys())
    repo_paths = [f"- **{name}**: `{info['path']}` ({info.get('type', 'unknown')} - {info.get('priority', 'medium')} priority)" 
                  for name, info in repo_config.items()]
    
    prompt = f"""
# Multi-Repository SFDC Field Dependency Analysis Request

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Fields to Analyze:** {len(field_names)} fields
**Repositories:** {len(repo_config)} repositories  
**Request Type:** Orchestration Services sync decision analysis

## Fields for Analysis:
{chr(10).join(f"- {field}" for field in field_names)}

## Repository Scope:
{chr(10).join(repo_paths)}

## Analysis Requirements:

For EACH repository, please analyze each field using this methodology:

### 1. **Staging Layer Analysis**
   - Search for field mapping in staging models
   - Check patterns: `{field_name}_c`, `cpq_{field_name}`, exact matches
   - Document column definitions and transformations
   - Look in: `src/models/staging/zuora/`, `src/models/staging/sfdc/`, `staging/`

### 2. **Foundational Layer Analysis** 
   - Search foundational models for field consumption
   - Focus on recurring revenue and price ramp models
   - Check fact table incorporation: `fact_*`, `dim_*`
   - Look in: `src/models/foundational/`, `foundational/`

### 3. **Functional Layer Analysis**
   - Search functional models for field usage
   - Focus on SFA/MBA reporting models: `sfa_*`, analytics models
   - Check business metrics calculations
   - Look in: `src/models/functional/`, `functional/`

### 4. **Cross-Repository Impact Assessment**
   - Identify shared dependencies between repositories
   - Look for `ref()` calls that might reference models using these fields
   - Assess downstream impact across all repositories

## Criticality Framework:
   - 🔴 **CRITICAL**: Used in multiple repos, core business processes
   - 🟡 **HIGH**: Important for analytics, used in 2+ repos  
   - 🟢 **MEDIUM**: Limited usage, single repo dependency
   - ⚫ **UNUSED**: No downstream dependencies found

## Expected Output:

### Per-Field Analysis:
For each field, provide:

**Field Name: `{field_names[0] if field_names else 'example_field'}`**

**Repository Usage:**
- **Repo1**: [Staging: X models, Foundational: Y models, Functional: Z models]
- **Repo2**: [Staging: X models, Foundational: Y models, Functional: Z models]

**Key Dependencies:**
- Critical models using this field
- Business logic dependencies  
- Cross-repo references

**Criticality:** [🔴/🟡/🟢/⚫] with rationale

**Recommendation:** [KEEP current sync / Alternative sync / EOL] 

**Business Justification:** Detailed reasoning based on usage evidence

**Risk Assessment:** Impact of changing sync method

### Summary Table:
| Field | Repos Affected | Critical Models | Recommendation | Risk Level |
|-------|---------------|-----------------|----------------|------------|
| field1 | 2/4 | 5 models | KEEP | HIGH |

## Analysis Tools:
Please use these tools systematically:
- `codebase_search`: For semantic analysis of field usage
- `grep`: For pattern matching across files  
- `read_file`: For detailed model examination
- `list_dir`: For repository structure exploration

## Focus Areas:
- Price ramp identification logic
- Revenue recognition calculations
- SFA quarterly analysis models  
- MBA reporting dependencies
- Digital-led renewal logic
- Cross-repository data flow
"""
    
    return prompt

def generate_analysis_commands(repo_config: Dict[str, Dict], field_names: List[str]) -> List[str]:
    """Generate command-line analysis commands for each repository"""
    
    commands = []
    
    for repo_name, repo_info in repo_config.items():
        repo_path = repo_info['path']
        
        # Basic grep commands
        for field in field_names:
            commands.append(f"# Analysis for {field} in {repo_name}")
            commands.append(f"cd {repo_path}")
            commands.append(f"grep -r -n '{field}' src/models/ || echo 'No matches found'")
            commands.append(f"grep -r -n '{field}_c' src/models/ || echo 'No matches found'")
            commands.append(f"grep -r -n 'cpq_{field}' src/models/ || echo 'No matches found'")
            commands.append("")
    
    return commands

def save_analysis_template(field_names: List[str], repo_config: Dict[str, Dict], output_file: str):
    """Save comprehensive analysis template"""
    
    template = {
        "analysis_metadata": {
            "date": datetime.now().isoformat(),
            "fields_count": len(field_names),
            "repositories_count": len(repo_config),
            "analyst": "Claude AI",
            "request_type": "Multi-Repository Orchestration Services Analysis"
        },
        "repositories": repo_config,
        "fields_analysis": {}
    }
    
    for field_name in field_names:
        template["fields_analysis"][field_name] = {
            "repository_usage": {repo_name: {
                "staging_models": [],
                "foundational_models": [], 
                "functional_models": [],
                "key_dependencies": []
            } for repo_name in repo_config.keys()},
            "cross_repo_dependencies": [],
            "criticality": "",
            "recommendation": "",
            "business_justification": "",
            "risk_assessment": "",
            "downstream_impact": ""
        }
    
    with open(output_file, 'w') as f:
        json.dump(template, f, indent=2)
    
    print(f"📄 Multi-repo analysis template saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='SFDC Field Analysis Helper - Multi-Repository Version')
    parser.add_argument('--fields', required=True,
                       help='Comma-separated list of fields to analyze')
    parser.add_argument('--repo-config', 
                       help='JSON config file with repository information')
    parser.add_argument('--repo-paths',
                       help='Comma-separated list of repository paths (alternative to config)')
    parser.add_argument('--output', default='multi_repo_analysis_template.json',
                       help='Output template filename')
    parser.add_argument('--prompt-only', action='store_true',
                       help='Only generate Claude prompt (no template file)')
    parser.add_argument('--generate-commands', action='store_true',
                       help='Generate shell commands for manual analysis')
    
    args = parser.parse_args()
    
    # Parse field list
    field_names = [field.strip() for field in args.fields.split(',')]
    
    # Load repository configuration
    repo_config = {}
    
    if args.repo_config:
        repo_config = load_repo_config(args.repo_config)
    elif args.repo_paths:
        # Simple path-based configuration
        repo_paths = [path.strip() for path in args.repo_paths.split(',')]
        for i, path in enumerate(repo_paths):
            repo_name = os.path.basename(path) or f"repo_{i+1}"
            repo_config[repo_name] = {
                "path": path,
                "type": "dbt" if "dbt" in repo_name.lower() else "unknown",
                "priority": "medium"
            }
    else:
        print("❌ Please provide either --repo-config or --repo-paths")
        return
    
    if not repo_config:
        print("❌ No valid repository configuration found")
        return
    
    # Validate repositories
    print("🔍 Validating repository paths...")
    valid_repos = validate_repositories(repo_config)
    
    if not valid_repos:
        print("❌ No valid repositories found")
        return
    
    print(f"\n📝 SFDC Multi-Repository Field Analysis")
    print(f"🎯 Fields: {', '.join(field_names)}")
    print(f"📁 Repositories: {len(valid_repos)} valid repositories")
    print("="*80)
    
    # Generate Claude prompt
    prompt = generate_multi_repo_claude_prompt(field_names, valid_repos)
    
    print("🤖 CLAUDE ANALYSIS PROMPT:")
    print("="*80)
    print(prompt)
    print("="*80)
    
    if args.generate_commands:
        print("\n🔧 MANUAL ANALYSIS COMMANDS:")
        print("="*80)
        commands = generate_analysis_commands(valid_repos, field_names)
        for cmd in commands:
            print(cmd)
        print("="*80)
    
    if not args.prompt_only:
        # Save analysis template
        save_analysis_template(field_names, valid_repos, args.output)
    
    print(f"""
💡 NEXT STEPS:

1. **Copy the prompt above** and paste it into your Claude conversation
2. **Claude will analyze across all {len(valid_repos)} repositories**
3. **Review cross-repository dependencies** and impact assessment
4. **Validate results** with business stakeholders
5. **Share comprehensive analysis** with Orchestration Services team

🚀 Multi-repository analysis ready!
""")

if __name__ == "__main__":
    main()
