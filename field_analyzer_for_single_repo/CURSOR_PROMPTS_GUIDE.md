# Cursor Chat Prompts for SFDC Field Analysis

This guide provides ready-to-use prompts for running SFDC field analysis in Cursor Chat.

## Available Prompts

### 🚀 **CURSOR_QUICK_PROMPT.txt** (Recommended)
**Use this for:** Standard field analysis requests
**When:** You have a list of fields and need comprehensive analysis
**Copy/Paste:** The entire content from this file into Cursor Chat

### 🧪 **CURSOR_TEST_PROMPT.txt**
**Use this for:** Verifying setup before running full analysis
**When:** First time using the system or troubleshooting
**Copy/Paste:** Use this to test that everything works

### 📋 **CURSOR_CHAT_PROMPT.md**
**Use this for:** Detailed analysis with customization options
**When:** You need to modify fields, repos, or analysis parameters
**Copy/Paste:** Edit the placeholders then copy the content

## Quick Start Workflow

### Step 1: Test Setup (First Time Only)
```
Copy content from: CURSOR_TEST_PROMPT.txt
Paste into Cursor Chat → Verify everything works
```

### Step 2: Run Analysis
```
Copy content from: CURSOR_QUICK_PROMPT.txt
Edit the field list if needed
Paste into Cursor Chat → Get comprehensive analysis
```

### Step 3: Customize (Optional)
```
Copy content from: CURSOR_CHAT_PROMPT.md
Edit fields, repo paths, analysis parameters
Paste into Cursor Chat → Get customized analysis
```

## Field List Examples

### Orchestration Services Common Fields:
```
subscription_model_type,is_price_ramp,cpq_opportunity_name,cpq_quote_business_type,cpq_quote_number,renewal_type,opportunity_id,opportunity_close_date,opportunity_sales_model,quote_id,custom_list_price
```

### Price Ramp Critical Fields:
```
subscription_model_type,is_price_ramp,cpq_opportunity_name,cpq_quote_number
```

### Revenue Recognition Fields:
```
cpq_opportunity_name,cpq_quote_business_type,cpq_quote_number,subscription_model_type
```

## Expected Results

After running any prompt, you should get:

✅ **Per-Field Analysis:**
- Usage evidence across staging/foundational/functional layers
- Criticality assessment (🔴/🟡/🟢/⚫)
- Sync recommendations (KEEP/Alternative/EOL)
- Business justification and risk assessment

✅ **Executive Summary:**
- Summary table with all fields
- Risk assessment for Orchestration Services
- Key insights and recommendations

✅ **Technical Details:**
- Specific models using each field
- Cross-repository dependencies
- Business logic impacts

## Troubleshooting

### Scripts Not Found
```bash
# Try alternative paths
ls -la ~/Downloads/sfdc_field_analyzer/
ls -la /Users/$(whoami)/Downloads/sfdc_field_analyzer/
```

### Python Script Issues
```bash
# Check Python availability
python3 --version
# Make scripts executable
chmod +x /root/Downloads/sfdc_field_analyzer/*.py
```

### Manual Analysis Fallback
If scripts don't work, use these manual commands:
```bash
grep -r "field_name" src/models/
find src/models/ -name "*.sql" | xargs grep -l "field_name"
```

## Integration with Team Workflow

1. **Request Comes In** → "Analyze these 5 fields for Orchestration Services"
2. **Use Quick Prompt** → Copy/paste CURSOR_QUICK_PROMPT.txt with field list
3. **Get Results** → Comprehensive analysis in 2-3 minutes
4. **Share with Team** → Results ready for Orchestration Services

## Tips for Best Results

- **Be specific with field names** - Include exact SFDC field names
- **Review results** - Validate findings with business stakeholders
- **Update field lists** - Modify prompts for different analysis requests
- **Save results** - Keep analysis outputs for future reference

---

🚀 **Ready to use! Start with CURSOR_TEST_PROMPT.txt to verify setup, then use CURSOR_QUICK_PROMPT.txt for analysis.**
