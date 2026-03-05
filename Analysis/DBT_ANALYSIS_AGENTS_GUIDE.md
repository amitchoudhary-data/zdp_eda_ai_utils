# DBT Analysis Agents Guide

This guide covers two specialized agents for analyzing DBT models and their data lineage:

1. **Column Level Model Analysis Agent** - Analyzes source references for specific columns in a DBT model
2. **Table Usage Finder Agent** - Finds all downstream usage of a table across repositories

---

## 1. Column Level Model Analysis Agent

### Purpose
Scans a DBT model to find all source references for specified columns/fields, identifying alias names and providing structured output.

### Usage

```bash
# Basic usage
python3 column_level_model_analyzer.py --model <model_name> --columns "<col1,col2,col3>"

# Examples
python3 column_level_model_analyzer.py --model dim_accounts --columns "instance_account_derived_type,instance_account_is_sandbox"

python3 column_level_model_analyzer.py --model stg_zuora_subscription --columns "subscription_model_type,is_price_ramp"

# Save output to file
python3 column_level_model_analyzer.py --model dim_accounts --columns "col1,col2" --output analysis.md

# Specify output format
python3 column_level_model_analyzer.py --model dim_accounts --columns "col1,col2" --format gsheets
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--model` | Yes | Name of the DBT model to analyze (without .sql extension) |
| `--columns` | Yes | Comma-separated list of columns to analyze |
| `--workspace` | No | Path to workspace root (default: auto-detect) |
| `--format` | No | Output format: `gsheets`, `markdown`, or `both` (default: both) |
| `--output` | No | Output file path (default: stdout) |

### Output Format

**Markdown Table:**
| Column/Field | Source Table | Column Name in source (if alias used) |
|:-------------|:-------------|:--------------------------------------|
| col1 | source_table_a | original_col1 |
| col2 | source_table_b | - |

**Google Sheets Format (tab-separated):**
```
Column/Field	Source Table	Column Name in source (if alias used)
col1	source_table_a	original_col1
col2	source_table_b	-
```

### Features

- ✅ Finds direct column references
- ✅ Detects COALESCE patterns with multiple sources
- ✅ Detects CASE WHEN patterns
- ✅ Resolves CTE references to ultimate sources
- ✅ Identifies alias names
- ✅ Maintains input column order in output
- ✅ Creates separate rows for multiple source references

### Guardrails

1. Output column sequence matches input column sequence
2. Creates separate row for each source reference (COALESCE, CASE WHEN, etc.)
3. Shows original column name when alias is used
4. Provides observations/assumptions at the end

---

## 2. Table Usage Finder Agent

### Purpose
Analyzes the usage of specific database tables and their columns across the multi-project DBT workspace, including complete lineage tracing.

### Usage

```bash
# Find all usage of a table
python3 table_usage_finder.py --table <table_name>

# Find usage of specific columns
python3 table_usage_finder.py --table <table_name> --columns "<col1,col2>"

# Examples
python3 table_usage_finder.py --table salesforce_lead_bcv

python3 table_usage_finder.py --table CLEANSED.SALESFORCE.SALESFORCE_LEAD_BCV --columns "id,email"

python3 table_usage_finder.py --table zuora_subscription --columns "subscription_model_type,is_price_ramp"

# Save output
python3 table_usage_finder.py --table zuora_subscription --output lineage.md
```

### Arguments

| Argument | Required | Description |
|----------|----------|-------------|
| `--table` | Yes | Table name (fully qualified or just table name) |
| `--columns` | No | Comma-separated columns to track (default: all) |
| `--workspace` | No | Path to workspace root (default: auto-detect) |
| `--format` | No | Output format: `gsheets`, `markdown`, or `both` (default: both) |
| `--output` | No | Output file path (default: stdout) |
| `--max-depth` | No | Maximum lineage depth (default: 5) |

### Output Format

**Markdown Table:**
| Column Name | Source Model | Used in model | Repository Name | Lineage till all downstream models |
|:------------|:-------------|:--------------|:----------------|:-----------------------------------|
| id | salesforce_lead_bcv | stg_salesforce_lead | zdp_dbt_finance | stg_salesforce_lead > int_leads > dim_leads |
| email | salesforce_lead_bcv | stg_salesforce_lead | zdp_dbt_customer | stg_salesforce_lead > int_leads |

**Google Sheets Format (tab-separated):**
```
Column Name	Source Model	Used in model	Repository Name	Lineage till all downstream models
id	salesforce_lead_bcv	stg_salesforce_lead	zdp_dbt_finance	stg_salesforce_lead > int_leads > dim_leads
```

### Capabilities

1. **Reference Search**
   - Finds `{{ source('schema', 'table') }}` references
   - Finds `{{ ref('model') }}` references
   - Finds direct table name references

2. **Column Usage Analysis**
   - Explicit selection (`SELECT col_a, col_b`)
   - Wildcard selection (`SELECT *`) - marks all columns as used
   - WHERE clause usage
   - JOIN condition usage
   - GROUP BY / ORDER BY usage

3. **Lineage Tracing**
   - Traces from source through intermediate models
   - Shows complete path to downstream models
   - Respects max depth to prevent infinite recursion

### Repositories Searched

- `zdp_dbt_finance`
- `zdp_dbt_customer`
- `zdp_dbt_regional_product_analytics`
- `zdp_cloud_dbt_eda_sales_marketing`

---

## Quick Reference

### Column Level Analysis

```bash
# Analyze specific columns in a model
python3 column_level_model_analyzer.py \
    --model dim_zuora_subscriptions_daily_snapshot \
    --columns "subscription_model_type,is_price_ramp,renewal_type"
```

### Table Usage Analysis

```bash
# Find all usage of a Zuora table
python3 table_usage_finder.py \
    --table zuora_subscription \
    --columns "model_type_c,price_ramp_c"
```

---

## Cursor AI Integration

These agents can also be invoked directly through Cursor AI chat:

### Column Level Analysis Prompt
```
Analyze the DBT model [MODEL_NAME] for the following columns: [COLUMNS]

Provide output in the format:
| Column/Field | Source Table | Column Name in source (if alias used) |
```

### Table Usage Finder Prompt
```
Find all usage of table [TABLE_NAME] and columns [COLUMNS] across all DBT repositories.

Provide output in the format:
| Column Name | Source Model | Used in model | Repository Name | Lineage till all downstream models |
```

---

## Example Analyses

### Example 1: Subscription Model Type Analysis

```bash
python3 column_level_model_analyzer.py \
    --model int_price_ramp_charges_daily_snapshot \
    --columns "is_price_ramp,subscription_model_type"
```

Expected output:
| Column/Field | Source Table | Column Name in source (if alias used) |
|:-------------|:-------------|:--------------------------------------|
| is_price_ramp | rpc | is_price_ramp |
| subscription_model_type | rpc | subscription_model_type |

### Example 2: Instance Account Analysis

```bash
python3 column_level_model_analyzer.py \
    --model dim_accounts \
    --columns "instance_account_derived_type,instance_account_is_sandbox"
```

### Example 3: Full Lineage of Zuora Subscription

```bash
python3 table_usage_finder.py \
    --table zuora_subscription \
    --format markdown \
    --output zuora_subscription_lineage.md
```

---

## Troubleshooting

### Model Not Found
- Ensure the model name matches exactly (without .sql extension)
- Check if the model exists in one of the supported repositories

### No Column References Found
- The column might be passed through SELECT *
- Check for alias variations
- Verify the column exists in the model

### Incomplete Lineage
- Increase `--max-depth` for deeper tracing
- Some models may use dynamic SQL that can't be statically analyzed

---

## Files

| File | Description |
|------|-------------|
| `column_level_model_analyzer.py` | Column source reference analyzer |
| `table_usage_finder.py` | Table usage and lineage finder |
| `DBT_ANALYSIS_AGENTS_GUIDE.md` | This documentation |

---

*Created for EDA Team - DBT Analysis Toolkit*





