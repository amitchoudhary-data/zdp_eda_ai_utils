# CURSOR CHAT PROMPT - SFDC Field Analysis Execution

Copy and paste this prompt into Cursor Chat to run SFDC field analysis:

---

## SFDC Field Analysis Request for Cursor Chat

I need you to help me run an automated SFDC field dependency analysis using the scripts saved in my Downloads folder.

### Background
I have a complete SFDC field analysis toolkit that generates structured prompts for Claude to analyze field dependencies across dbt repositories. The toolkit was designed to replace manual 2-3 day analysis with automated 2-3 minute analysis using Claude's codebase search capabilities.

### Available Scripts
Please check for these files in `/root/Downloads/sfdc_field_analyzer/` (or `~/Downloads/sfdc_field_analyzer/`):

1. `simple_field_analyzer.py` - Single repository analysis
2. `sfdc_field_analyzer_local.py` - Multi-repository analysis
3. `repos_config_example.json` - Repository configuration template
4. `README_LOCAL_SETUP.md` - Setup instructions
5. `SFDC_ZUORA_FIELD_ANALYSIS_CHECKLIST.md` - Analysis methodology

### Task: Run Field Analysis

**Fields to analyze:** [REPLACE WITH YOUR FIELDS]
```
subscription_model_type,is_price_ramp,cpq_opportunity_name,cpq_quote_business_type,renewal_type
```

**Analysis type needed:**
- [ ] Single repository (current workspace)
- [ ] Multi-repository (specify paths below)

**Repository paths (if multi-repo):**
```
/workspaces/zdp_dbt_finance
[ADD OTHER REPO PATHS HERE]
```

### Step-by-Step Execution

Please perform these steps:

#### 1. **Verify Script Availability**
```bash
ls -la /root/Downloads/sfdc_field_analyzer/
# or
ls -la ~/Downloads/sfdc_field_analyzer/
```

#### 2. **Choose Analysis Method**

**Option A: Single Repository Analysis**
```bash
cd [CURRENT_WORKSPACE_PATH]
python3 /root/Downloads/sfdc_field_analyzer/simple_field_analyzer.py \
  --fields="[FIELD_LIST]" \
  --prompt-only
```

**Option B: Multi-Repository Analysis**
```bash
python3 /root/Downloads/sfdc_field_analyzer/sfdc_field_analyzer_local.py \
  --fields="[FIELD_LIST]" \
  --repo-paths="[REPO_PATH_1],[REPO_PATH_2]" \
  --prompt-only
```

#### 3. **Execute Generated Analysis**

The script will output a structured Claude analysis prompt. **IMPORTANT:** Instead of just showing me the prompt, please **execute the analysis directly** using your available tools:

- Use `codebase_search` for semantic field analysis
- Use `grep` for pattern matching across repositories
- Use `read_file` for examining specific models
- Use `list_dir` for repository exploration

Follow this systematic methodology for each field:

**Staging Layer Analysis:**
- Search for field mapping in `staging/zuora/` and `staging/sfdc/` models
- Look for patterns: `{field_name}`, `{field_name}_c`, `cpq_{field_name}`
- Check column definitions and transformations

**Foundational Layer Analysis:**
- Search `foundational/` models for field consumption
- Focus on recurring revenue and price ramp models
- Check fact table incorporation: `fact_*`, `dim_*` models
- Identify dimension table references

**Functional Layer Analysis:**
- Search `functional/` models for field usage
- Focus on SFA/MBA reporting models: `sfa_*` models
- Check digital-led renewal logic dependencies
- Identify business metrics calculations

**Criticality Assessment:**
- 🔴 CRITICAL: Essential for core business processes
- 🟡 HIGH: Important for analytics and reporting
- 🟢 MEDIUM: Limited usage, alternative options exist
- ⚫ UNUSED: No downstream dependencies found

#### 4. **Generate Comprehensive Report**

For each field, provide:

**Field Name: `[field_name]`**
- **Usage Evidence:** Specific models and patterns found
- **Staging Usage:** [List of staging models]
- **Foundational Usage:** [List of foundational models]
- **Functional Usage:** [List of functional models]
- **Key Dependencies:** Critical business logic using this field
- **Criticality:** [🔴/🟡/🟢/⚫] with detailed rationale
- **Recommendation:** [KEEP current sync / Alternative sync / EOL recommended]
- **Business Justification:** Why this recommendation makes sense
- **Downstream Impact:** What breaks if sync method changes
- **Risk Assessment:** High/Medium/Low risk for modification

#### 5. **Summary & Recommendations**

Provide executive summary:

| Field | Criticality | Recommendation | Models Affected | Risk Level |
|-------|-------------|---------------|-----------------|------------|
| field1 | 🔴 CRITICAL | KEEP current sync | 15 models | HIGH |
| field2 | 🟢 MEDIUM | Alternative sync | 3 models | LOW |

**Key Insights:**
- Fields critical to price ramp identification
- Revenue recognition dependencies
- Cross-repository impact assessment
- Business continuity considerations

### Expected Output Format

Please provide:
1. **Script execution results** (confirm files found and scripts run)
2. **Direct field analysis** (using your codebase search tools)
3. **Comprehensive field-by-field assessment**
4. **Executive summary with recommendations**
5. **Risk assessment for Orchestration Services**

### Analysis Focus Areas
Pay special attention to:
- Price ramp identification logic (`int_price_ramp_*` models)
- Revenue recognition calculations (`fact_recurring_revenue_*`)
- SFA quarterly analysis models (`sfa_qtd_*`)
- MBA reporting dependencies
- Digital-led renewal logic
- SFDC field mapping and transformations

### Business Context
This analysis supports Orchestration Services team decisions on:
- Which SFDC→Zuora field syncs to maintain real-time
- Which fields can use alternative sync methods
- Which fields can be EOL'd entirely
- Risk assessment for changing sync patterns

Please execute this analysis systematically and provide actionable recommendations for the Orchestration Services team.

---

## Alternative Quick Commands

If the scripts aren't available, you can run manual analysis using these commands:

```bash
# Search for specific fields across codebase
grep -r -n "subscription_model_type\|is_price_ramp\|cpq_opportunity_name" src/models/

# Check staging layer usage
find src/models/staging/ -name "*.sql" -o -name "*.yml" | xargs grep -l "field_name"

# Check foundational layer usage
find src/models/foundational/ -name "*.sql" -o -name "*.yml" | xargs grep -l "field_name"

# Check functional layer usage
find src/models/functional/ -name "*.sql" -o -name "*.yml" | xargs grep -l "field_name"
```

Execute the analysis and provide comprehensive results!
