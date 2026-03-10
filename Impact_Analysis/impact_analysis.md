# 📊 DBT Impact Analysis Template

> **Purpose:** Analyze field/column dependencies, lineage, and impact across DBT repositories.

---

## 🎯 User Input Section

### Required Information

| Input | Your Value |
|:------|:-----------|
| **Model Name** | `[Enter DBT model name without .sql]` |
| **Columns to Analyze** | `[col1, col2, col3]` |
| **Repositories to Search** | `[zdp_dbt_customer, zdp_dbt_finance, etc.]` |

### Analysis Options

- [ ] **Upstream Analysis** - Find source origins of columns
- [ ] **Downstream Analysis** - Find all consuming models
- [ ] **Full Lineage** - Both upstream and downstream
- [ ] **Cross-Repository Impact** - Analyze across all repos

> ❓ **Do you want upstream details?** (Source tables, original column names, transformations)
> 
> ❓ **Do you want downstream details?** (All consuming models, lineage paths, leaf nodes)

---

## 📋 Analysis Type 1: Column Level Source Analysis

### Purpose
Find all source references for specified columns in a DBT model, including aliases.

### Input
```
Model: [YOUR_MODEL_NAME]
Columns: [col1, col2, col3]
```

### Output Format (Google Sheets Copy-Paste)

```
Column/Field	Source Table	Column Name in Source (if alias used)	Transformation
[col1]	[source_table]	[original_name or -]	[Direct/COALESCE/CASE WHEN/etc.]
```

### Example Output

| Column/Field | Source Table | Column Name in Source | Transformation |
|:-------------|:-------------|:----------------------|:---------------|
| instance_account_derived_type | int_instance_accounts_derived_type | instance_account_derived_type | CASE WHEN logic |
| instance_account_is_sandbox | int_instance_accounts_bq_dim_instance_accounts | sandbox_master_id IS NOT NULL | COALESCE + Boolean |

### Observations
- [ ] List any assumptions made
- [ ] Note any complex transformations
- [ ] Flag any columns not found

---

## 📋 Analysis Type 2: Table/Model Usage Finder

### Purpose
Find all downstream models that reference a given table/model and trace lineage to leaf nodes.

### Input
```
Table/Model: [YOUR_TABLE_OR_MODEL]
Columns (optional): [col1, col2]
Max Depth: [5]
```

### Output Format (Google Sheets Copy-Paste)

```
Column Name	Source Model	Used in Model	Repository Name	Lineage Path
[col1]	[source]	[downstream_model]	[repo_name]	[model1 > model2 > model3]
```

### Example Output

| Column Name | Source Model | Used in Model | Repository | Lineage Path |
|:------------|:-------------|:--------------|:-----------|:-------------|
| instance_account_derived_type | int_instance_accounts_derived_type | dim_instance_accounts_daily_snapshot | zdp_dbt_customer | int_... > dim_... > bcv |
| instance_account_is_sandbox | int_instance_accounts_bq_dim_instance_accounts | int_instance_accounts_product | zdp_dbt_customer | int_bq > int_product > ... |

---

## 📋 Analysis Type 3: Full Impact Assessment

### Upstream Lineage (Source → Target)

```
┌─────────────────────────────────────────────────────────────┐
│ [ULTIMATE SOURCE TABLE]                                      │
│ Database: [schema.table]                                     │
│ Columns: [list source columns]                               │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ [STAGING MODEL]                                              │
│ Model: stg_[source]                                          │
│ Transformation: [describe]                                   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│ [TARGET MODEL]                                               │
│ Model: [your model]                                          │
│ Columns analyzed: [col1, col2]                               │
└─────────────────────────────────────────────────────────────┘
```

### Downstream Lineage (Target → Consumers)

```
┌─────────────────────────────────────────────────────────────┐
│ [YOUR MODEL]                                                 │
└─────────────────────────────────────────────────────────────┘
          │
          ├────────────────────┬────────────────────┐
          ▼                    ▼                    ▼
    [Consumer 1]         [Consumer 2]         [Consumer 3]
          │                    │                    │
          ▼                    ▼                    ▼
      [Mart 1]             [Mart 2]             [Mart 3]
          │                    │                    │
          ▼                    ▼                    ▼
      [BCV/Leaf]           [BCV/Leaf]          [BCV/Leaf]
```

---

## 🔴 Criticality Assessment

| Criticality | Definition | Criteria |
|:------------|:-----------|:---------|
| 🔴 **CRITICAL** | Core business logic | Used in 3+ repos, revenue/billing impact |
| 🟡 **HIGH** | Important analytics | Used in 2 repos, key reporting |
| 🟢 **MEDIUM** | Limited scope | Single repo, non-critical |
| ⚫ **UNUSED** | No dependencies | Safe to deprecate |

### Per-Column Criticality

| Column | Upstream Sources | Downstream Consumers | Cross-Repo | Criticality |
|:-------|:-----------------|:---------------------|:-----------|:------------|
| col1 | 2 | 5 | Yes | 🔴 |
| col2 | 1 | 2 | No | 🟢 |

---

## 🔄 Refresh Order (Topological Sort)

### Models to Refresh

| Order | Model Name | Repository | Layer | Dependencies |
|:------|:-----------|:-----------|:------|:-------------|
| 1 | [source_model] | [repo] | Staging | - |
| 2 | [int_model] | [repo] | Intermediate | 1 |
| 3 | [fact_model] | [repo] | Mart | 2 |
| 4 | [bcv_model] | [repo] | BCV | 3 |

### dbt Commands

```bash
# Option 1: Run specific models in order
dbt run --select [model1]
dbt run --select [model2]
dbt run --select [model3]

# Option 2: Run with downstream (+)
dbt run --select [source_model]+

# Option 3: Run by tag
dbt run --select tag:[your_tag]
```

---

## 📝 Summary Report

### Analysis Summary

| Metric | Value |
|:-------|------:|
| Total Columns Analyzed | X |
| Upstream Sources Found | X |
| Downstream Consumers | X |
| Repositories Impacted | X |
| Leaf/Terminal Nodes | X |

### Recommendations

| Column | Recommendation | Risk | Justification |
|:-------|:---------------|:-----|:--------------|
| col1 | KEEP | HIGH | Critical for revenue reporting |
| col2 | DEPRECATE | LOW | No downstream usage |

### Risk Assessment

| Risk Level | Description |
|:-----------|:------------|
| 🔴 HIGH | Changes will impact production dashboards |
| 🟡 MEDIUM | Changes require coordination |
| 🟢 LOW | Safe to proceed |

---

## 🛠️ Cursor AI Prompts

### For Column Source Analysis
```
Analyze the DBT model [MODEL_NAME] for the following columns: [COLUMNS]

Find all source references for each column including:
- Source table name
- Original column name if alias is used
- Transformation type (direct, COALESCE, CASE WHEN, etc.)

Output in gsheets format:
Column/Field | Source Table | Column Name in Source | Transformation
```

### For Downstream Lineage
```
Find all downstream usage of model [MODEL_NAME] across repositories:
- zdp_dbt_customer
- zdp_dbt_finance  
- zdp_dbt_regional_product_analytics
- zdp_cloud_dbt_eda_sales_marketing
check in all repos where the promt is running


For each downstream model, provide:
- Repository name
- Full lineage path to leaf nodes
- Columns used (explicit or SELECT *)
```

### For Full Impact Analysis
```
Perform full impact analysis for columns [COLUMNS] in model [MODEL_NAME]:

1. UPSTREAM: Find all source origins
2. DOWNSTREAM: Find all consuming models
3. CROSS-REPO: Check all repositories
4. REFRESH ORDER: Provide topological sort
5. CRITICALITY: Assess risk level

# Criticality Framework:
   - 🔴 **CRITICAL**: Used in multiple repos, core business 
   processes
   - 🟡 **HIGH**: Important for analytics, used in 2+ repos  
   - 🟢 **MEDIUM**: Limited usage, single repo dependency
   - ⚫ **UNUSED**: No downstream dependencies found
Include both upstream and downstream details.
```

---

## 🌐 GitHub MCP: Org-Wide Analysis (Hybrid Approach)

### Why Local-Only Analysis is Insufficient

The local workspace contains ~17 cloned repos. The `zendesk` GitHub org has **161+ `zdp_dbt` repositories**. Local-only analysis misses:

| What You Miss | Where It Lives | Why It Matters |
|:--------------|:---------------|:---------------|
| Looker BI views (`.lkml`) | `looker-zdp` | Column renames break dashboards |
| Data contracts & ownership | `zdp-data-contract-sync-python` | Criticality tags, Alation URLs, team ownership |
| Non-cloned DBT repos | 140+ repos not in workspace | Hidden downstream consumers |
| Commit history & authors | GitHub API | Recent changes, who to contact |
| Legacy table variants | `ZDP.PUBLIC.*` entries | Old versions may still have consumers |
| ML notebooks & ad-hoc queries | `eda-recommendations-ml-models`, `gao_product_analytics` | Non-DBT SQL consumers |

### GitHub MCP Tools

| Tool | Purpose | Example |
|:-----|:--------|:--------|
| `search_code` | Find all references across entire org | `"model_name org:zendesk language:sql"` |
| `get_file_contents` | Read files from repos not cloned locally | `owner=zendesk, repo=looker-zdp, path=...` |
| `list_commits` | Recent change history and authors | `owner=zendesk, repo=zdp_dbt_finance` |
| `search_repositories` | Discover all `zdp_dbt` repos in org | `"zdp_dbt org:zendesk"` |
| `get_repository_tree` | Explore directory structure of any repo | `owner=zendesk, repo=..., recursive=true` |

### Hybrid Analysis Workflow

```
Step 1: GitHub MCP Broad Search
   ├── search_code: "model_name org:zendesk language:sql"     (SQL references)
   ├── search_code: "model_name org:zendesk language:yaml"    (source definitions)
   ├── search_code: "model_name org:zendesk repo:looker-zdp"  (Looker views)
   └── search_code: "MODEL_NAME org:zendesk repo:zdp-data-contract-sync-python" (data contracts)

Step 2: GitHub MCP Deep Dive
   ├── get_file_contents: Read SQL/LookML from non-local repos
   └── list_commits: Get recent changes and authors

Step 3: Local Workspace Deep Analysis
   ├── Read macro/Jinja logic (complex multi-file analysis)
   ├── Trace ref() and source() chains
   └── Analyze config blocks and materializations

Step 4: Compile Hybrid Report
   └── Merge findings into unified impact analysis
```

### Search Syntax Quick Reference

```bash
# All SQL references across org
"model_name org:zendesk language:sql"

# YAML source definitions
"model_name org:zendesk language:yaml"

# Looker views only
"model_name org:zendesk repo:looker-zdp"

# Data contracts only
"MODEL_NAME org:zendesk repo:zdp-data-contract-sync-python"

# Specific repo search
"model_name org:zendesk repo:zdp_dbt_finance"

# Filter by path
"model_name org:zendesk path:models/functional"

# Exclude test files
"model_name org:zendesk language:sql NOT path:test"
```

### Validated Case Studies

**`dim_instance_accounts`:**

| Metric | Local Only | GitHub MCP Hybrid |
|:-------|:-----------|:------------------|
| Repos searched | ~17 | **161+** |
| Repos with matches | 8 | **26** (+17 new) |
| Key new repos | - | `eda_da3_enrichment`, `zdp_dbt_data_delivery_service`, `zdp_dbt_resilience`, `zdp_dbt_sre_engage`, `zdp_dbt_growth_engine`, `looker-zdp` |

**`SFA_QTD_CHANGE_SUBTYPE_UNADJ_CURRENT`:**

| Metric | Local Only | GitHub MCP Hybrid |
|:-------|:-----------|:------------------|
| DBT downstream | 5 models / 2 repos | Same |
| Looker BI views | **Not found** | **3 views** (53+ dimensions) |
| Data contracts | **Not found** | **6 entries** + Alation URL |
| Legacy variants | **Not found** | **5 `ZDP.PUBLIC` versions** |
| Commit history | **Not available** | Full history with authors |
| Team ownership | **Unknown** | `eda-platform` |

### Output Format: Hybrid Comparison Table

Include this table in every hybrid analysis to show what the GitHub MCP discovered beyond local:

| What was found | Local Only | GitHub MCP Hybrid |
|:---------------|:-----------|:------------------|
| DBT model definition | Yes/No | Yes/No |
| Within-repo downstream | X models | X models |
| Cross-repo DBT consumers | X repos | X repos |
| Looker BI layer | Not found | X views |
| Data contracts/governance | Not found | X entries |
| Legacy table versions | Not found | X variants |
| Commit history | Not available | X recent commits |
| Team ownership | Unknown | [team name] |

---

## 📚 Repositories Covered

### Local Workspace (~17 repos)

| Repository | Description | Path |
|:-----------|:------------|:-----|
| zdp_dbt_customer | Customer domain models | `zdp_dbt_customer/src/models/` |
| zdp_dbt_finance | Finance domain models | `zdp_dbt_finance/src/models/` |
| zdp_dbt_regional_product_analytics | Regional analytics | `zdp_dbt_regional_product_analytics/src/models/` |
| zdp_cloud_dbt_eda_sales_marketing | EDA Sales/Marketing | `zdp_cloud_dbt_eda_sales_marketing/models/` |
| zdp_cloud_dbt_customer_experience | Customer Experience | `zdp_cloud_dbt_customer_experience/models/` |
| zdp_cloud_dbt_growth_analytics | Growth Analytics | `zdp_cloud_dbt_growth_analytics/models/` |
| zdp_cloud_dbt_eda_finance | EDA Finance | `zdp_cloud_dbt_eda_finance/models/` |
| zdp_dbt_enterprise_data_ml | ML / Decision Science | `zdp_dbt_enterprise_data_ml/src/models/` |
| zdp_dbt_regional_accounts | Accounts (foundational) | `zdp_dbt_regional_accounts/src/models/` |
| zdp_dbt_product_analytics | Product Analytics | `zdp_dbt_product_analytics/src/models/` |

### GitHub MCP Only (key repos not in local workspace)

| Repository | Description | Why It Matters |
|:-----------|:------------|:---------------|
| `looker-zdp` | Looker view definitions (`.lkml`) | BI/dashboard layer -- column changes break views |
| `zdp-data-contract-sync-python` | Data contracts, tags, Alation URLs | Ownership, criticality, catalog links |
| `zdp_dbt_data_delivery_service` | Data delivery pipelines | Customer/finance/product data integrations |
| `zdp_dbt_regional_support` | Regional support models | `dim_instance_ticket_resolved` definition |
| `zdp_dbt_regional_sre_capacity` | SRE capacity planning | Aggregated ticket capacity models |
| `eda_da3_enrichment` | DA3 enrichment pipeline | Enriched instance account models |
| `zdp_dbt_growth_engine` | Growth engine models | Customer account pod mappings |
| `zdp_dbt_resilience` | Incident detection (CID) | Ranked subdomains for reliability |
| `zdp_dbt_sre_engage` | SLA reporting | Premier account filtering |
| `zdp_dbt_technology_alliances` | Marketplace metrics | App install dashboards |
| `zdp_sqldbm_models` | SqlDBM documentation | Data modeling reference |

---

## ✅ Checklist

- [ ] Identified model to analyze
- [ ] Listed columns/fields
- [ ] Selected analysis type (upstream/downstream/both)
- [ ] Ran column source analysis
- [ ] Ran downstream lineage analysis
- [ ] **GitHub MCP: Searched entire zendesk org** (`search_code`)
- [ ] **GitHub MCP: Checked Looker views** (`repo:looker-zdp`)
- [ ] **GitHub MCP: Checked data contracts** (`repo:zdp-data-contract-sync-python`)
- [ ] **GitHub MCP: Read files from non-local repos** (`get_file_contents`)
- [ ] **GitHub MCP: Checked commit history** (`list_commits`)
- [ ] Assessed criticality
- [ ] Determined refresh order
- [ ] Documented recommendations
- [ ] Compiled hybrid comparison table

### Summary Table:

| Field | Repos Affected | Critical Models | Looker Views | Data Contracts | Recommendation | Risk Level |
|:------|:---------------|:----------------|:-------------|:---------------|:---------------|:-----------|
| field1 | 2/4 (local) + N (MCP) | 5 models | X views | X entries | KEEP | HIGH |

## Analysis Tools:

### Local Workspace
- `codebase_search`: For semantic analysis of field usage
- `grep`: For pattern matching across files
- `read_file`: For detailed model examination
- `list_dir`: For repository structure exploration

### GitHub MCP (Org-Wide)
- `search_code`: Search all 161+ repos in zendesk org
- `get_file_contents`: Read files from any repo
- `list_commits`: Commit history and authors
- `search_repositories`: Discover repos
- `get_repository_tree`: Explore repo structure

## Focus Areas:
- Price ramp identification logic
- Revenue recognition calculations
- SFA quarterly analysis models
- MBA reporting dependencies
- Digital-led renewal logic
- Cross-repository data flow
- **Looker BI layer impact** (via GitHub MCP)
- **Data contract compliance** (via GitHub MCP)
