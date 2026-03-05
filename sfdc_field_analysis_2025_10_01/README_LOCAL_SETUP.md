# SFDC Field Analysis - Local Multi-Repository Setup

## Overview

This toolkit enables automated SFDC field dependency analysis across multiple local repositories using Claude AI. Perfect for Orchestration Services requests and cross-repo impact assessment.

## Files Included

- `simple_field_analyzer.py` - Basic single-repo analysis
- `sfdc_field_analyzer_local.py` - Multi-repository analysis  
- `repos_config_example.json` - Repository configuration template
- `README_LOCAL_SETUP.md` - This setup guide

## Quick Start

### 1. **Save Files Locally**

```bash
# Create project directory
mkdir ~/sfdc_field_analyzer
cd ~/sfdc_field_analyzer

# Download the files (copy content from the scripts)
curl -o simple_field_analyzer.py [URL_TO_SCRIPT]
curl -o sfdc_field_analyzer_local.py [URL_TO_SCRIPT]  
curl -o repos_config_example.json [URL_TO_CONFIG]
```

### 2. **Configure Your Repositories**

```bash
# Copy example config and customize
cp repos_config_example.json my_repos.json

# Edit with your actual repository paths
nano my_repos.json
```

**Update paths in `my_repos.json`:**
```json
{
  "repositories": {
    "zdp_dbt_finance": {
      "path": "/Users/yourname/work/zdp_dbt_finance",
      "type": "dbt",
      "priority": "high"
    },
    "zdp_dbt_core": {
      "path": "/Users/yourname/work/zdp_dbt_core", 
      "type": "dbt",
      "priority": "high"
    }
  }
}
```

### 3. **Run Analysis**

**Option A: Single Repository**
```bash
cd /path/to/your/dbt/project
python ~/sfdc_field_analyzer/simple_field_analyzer.py --fields="subscription_model_type,is_price_ramp"
```

**Option B: Multiple Repositories**
```bash
python ~/sfdc_field_analyzer/sfdc_field_analyzer_local.py \
  --fields="renewal_type,model_type,opportunity_name" \
  --repo-config="my_repos.json"
```

**Option C: Quick Multi-Repo (No Config)**
```bash
python ~/sfdc_field_analyzer/sfdc_field_analyzer_local.py \
  --fields="field1,field2" \
  --repo-paths="/path/repo1,/path/repo2,/path/repo3"
```

## Usage Examples

### Example 1: Orchestration Services Request
```bash
# Analyze 5 fields across 3 repositories
python sfdc_field_analyzer_local.py \
  --fields="renewal_type,model_type,opportunity_name,quote_number,is_price_ramp" \
  --repo-config="my_repos.json" \
  --output="orchestration_analysis.json"

# This generates:
# 1. Claude analysis prompt (copy/paste to Claude)
# 2. Analysis template JSON file
# 3. Repository validation results
```

### Example 2: Quick Single Field Check
```bash
# Check one critical field
python simple_field_analyzer.py \
  --fields="subscription_model_type" \
  --prompt-only
```

### Example 3: Generate Manual Commands
```bash
# Get shell commands for manual grep analysis
python sfdc_field_analyzer_local.py \
  --fields="cpq_opportunity_name" \
  --repo-config="my_repos.json" \
  --generate-commands
```

## What The Scripts Do

### `simple_field_analyzer.py`
- ✅ **Generates Claude prompts** for systematic analysis
- ✅ **Works with single repository** (current directory)
- ✅ **Creates analysis templates** for tracking results
- ✅ **No external dependencies** or complex setup

### `sfdc_field_analyzer_local.py`
- ✅ **Multi-repository analysis** across your local projects
- ✅ **Repository validation** (checks paths exist)
- ✅ **Cross-repo impact assessment** 
- ✅ **Configurable search patterns** and focus areas
- ✅ **Manual command generation** for backup analysis

### Key Features:
- **No API calls** - Just generates prompts for Claude
- **No git cloning** - Uses your existing local repositories
- **No external tools** - Pure Python with standard library
- **Flexible configuration** - JSON config or command-line paths

## Claude Analysis Workflow

1. **Run script** → Get structured analysis prompt
2. **Copy prompt** → Paste into Claude conversation  
3. **Claude analyzes** → Uses available tools (codebase_search, grep)
4. **Get results** → Comprehensive field dependency analysis
5. **Share with team** → Ready for Orchestration Services

## Sample Output

```
📝 SFDC Multi-Repository Field Analysis
🎯 Fields: renewal_type, model_type
📁 Repositories: 3 valid repositories
================================================================================

✅ zdp_dbt_finance: /Users/name/work/zdp_dbt_finance
✅ zdp_dbt_core: /Users/name/work/zdp_dbt_core  
❌ zdp_dbt_marketing: Path not found - /invalid/path

🤖 CLAUDE ANALYSIS PROMPT:
================================================================================
# Multi-Repository SFDC Field Dependency Analysis Request

**Date:** 2025-09-25 18:00:00
**Fields to Analyze:** 2 fields
**Repositories:** 2 repositories
...
[Full structured prompt for Claude]
================================================================================
```

## Troubleshooting

### Repository Path Issues
```bash
# Check paths exist
ls /path/to/your/repo

# Update config file
nano my_repos.json
```

### Permission Issues
```bash
# Make scripts executable
chmod +x simple_field_analyzer.py
chmod +x sfdc_field_analyzer_local.py
```

### Python Dependencies
```bash
# Check Python version (3.6+ required)
python3 --version

# No external packages needed - uses standard library only
```

## Advanced Configuration

### Custom Search Patterns
Edit `my_repos.json` to customize field search patterns:
```json
{
  "analysis_settings": {
    "field_patterns": [
      "{field_name}",
      "{field_name}_c", 
      "cpq_{field_name}",
      "custom_{field_name}_pattern"
    ]
  }
}
```

### Repository Priorities
Set priority levels to focus analysis:
```json
{
  "repositories": {
    "critical_repo": {
      "priority": "high"    // Analyzed first
    },
    "optional_repo": {
      "priority": "low"     // Analyzed if needed
    }
  }
}
```

## Integration with Team Workflow

### Standardized Process
1. **Request comes in** → "Analyze these 5 fields for Orchestration Services"
2. **Run script** → Generate analysis prompt  
3. **Claude analyzes** → Get comprehensive results in 2-3 minutes
4. **Team review** → Validate with business stakeholders
5. **Deliver results** → Share with Orchestration Services team

### Output Formats
- **Claude conversation** → Rich interactive analysis
- **JSON template** → Structured data for tracking
- **Shell commands** → Manual backup analysis option

This replaces **days of manual analysis** with **minutes of automated analysis** while maintaining the same quality and thoroughness.

## Next Steps

1. **Save scripts locally** using the provided files
2. **Configure your repositories** in `my_repos.json`
3. **Test with sample fields** to validate setup
4. **Integrate into team workflow** for Orchestration Services requests
5. **Scale analysis capacity** across EDA team

🚀 **You now have a complete local multi-repository SFDC field analysis system!**
