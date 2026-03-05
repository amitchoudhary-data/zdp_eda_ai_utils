# SFDC Field Analysis with Claude CLI

Automated SFDC field dependency analysis tool that can work with Claude CLI for direct analysis execution.

## 🚀 Quick Start

### Basic Usage (Display Prompt)
```bash
python3 simple_field_analyzer.py --fields="subscription_model_type,is_price_ramp,cpq_opportunity_name"
```

### With Claude CLI (Direct Analysis)
```bash
python3 simple_field_analyzer.py \
  --fields="subscription_model_type,is_price_ramp" \
  --claude-cli
```

### With Specific Claude Model
```bash
python3 simple_field_analyzer.py \
  --fields="subscription_model_type,is_price_ramp" \
  --claude-cli \
  --model="claude-sonnet-4-20250514"
```

## 📋 Prerequisites

### For Manual Mode (Default)
- Python 3.x
- No additional dependencies

### For Claude CLI Mode
1. Install Claude CLI:
   ```bash
   npm install -g @anthropic-ai/claude-cli
   ```

2. Configure your API key:
   ```bash
   export ANTHROPIC_API_KEY="your-api-key"
   ```

## 🎯 Command Line Options

| Option | Description | Example |
|--------|-------------|---------|
| `--fields` | **Required.** Comma-separated list of SFDC fields to analyze | `--fields="field1,field2,field3"` |
| `--claude-cli` | Send prompt directly to Claude CLI for automated analysis | `--claude-cli` |
| `--model` | Specify Claude model to use (requires --claude-cli) | `--model="claude-sonnet-4-20250514"` |
| `--output` | Output filename for analysis template (default: field_analysis_template.json) | `--output="my_analysis.json"` |
| `--prompt-only` | Only generate prompt, don't save template file | `--prompt-only` |

## 📊 Analysis Output

The tool provides comprehensive analysis including:

- ✅ **Staging Layer Analysis** - Field mapping and transformations
- ✅ **Foundational Layer Analysis** - Revenue models and fact table usage
- ✅ **Functional Layer Analysis** - SFA/MBA reporting dependencies
- ✅ **Criticality Assessment** - CRITICAL/HIGH/MEDIUM/UNUSED classification
- ✅ **Sync Recommendations** - KEEP/Alternative/EOL recommendations
- ✅ **Business Impact** - Downstream effects and risk assessment

## 🔧 Usage Examples

### Example 1: Analyze Price Ramp Fields
```bash
python3 simple_field_analyzer.py \
  --fields="subscription_model_type,is_price_ramp" \
  --claude-cli
```

### Example 2: Analyze CPQ Fields (Manual Mode)
```bash
python3 simple_field_analyzer.py \
  --fields="cpq_opportunity_name,cpq_quote_business_type,cpq_quote_number" \
  --output="cpq_fields_analysis.json"
```

### Example 3: Quick Analysis (No Template File)
```bash
python3 simple_field_analyzer.py \
  --fields="renewal_type" \
  --claude-cli \
  --prompt-only
```

## 📁 Output Files

### JSON Template (Optional)
When not using `--prompt-only`, generates a structured JSON template:
```json
{
  "analysis_metadata": {
    "date": "2025-10-01T...",
    "fields_count": 2,
    "analyst": "Claude AI",
    "request_type": "Orchestration Services"
  },
  "fields": {
    "field_name": {
      "staging_usage": [],
      "foundational_usage": [],
      "functional_usage": [],
      "criticality": "",
      "recommendation": "",
      "rationale": "",
      "downstream_impact": "",
      "business_justification": ""
    }
  }
}
```

## 🤖 Claude CLI Integration

### How It Works
1. Script generates structured analysis prompt
2. Sends prompt to Claude CLI with specified model
3. Claude analyzes fields using codebase search tools
4. Results displayed directly in terminal

### Fallback Behavior
If Claude CLI fails or is not installed:
- Script automatically falls back to manual mode
- Displays prompt for copy/paste into Claude interface
- Optionally saves JSON template for manual tracking

## 🔍 Analysis Methodology

The tool follows a systematic approach:

1. **Source Identification** - Find field in Zuora/SFDC staging
2. **Lineage Tracing** - Track through staging → foundational → functional
3. **Usage Patterns** - Identify where field is used in business logic
4. **Impact Assessment** - Determine criticality and downstream effects
5. **Recommendations** - Provide sync strategy recommendations

## 📈 Real-World Analysis Results

### Critical Fields (KEEP current sync)
- `subscription_model_type` - Price ramp identification
- `is_price_ramp` - Revenue blending logic

### Medium Fields (Alternative sync acceptable)
- `cpq_opportunity_name` - Reference only, no calculations
- `cpq_quote_business_type` - Metadata field

### Calculated Fields (No sync needed)
- `renewal_type` - Derived in dbt, not source field

## 🛠️ Troubleshooting

### Claude CLI Not Found
```bash
# Install Claude CLI
npm install -g @anthropic-ai/claude-cli

# Verify installation
claude --version
```

### API Key Issues
```bash
# Set API key
export ANTHROPIC_API_KEY="sk-ant-..."

# Or add to ~/.zshrc or ~/.bashrc
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
```

### Python Version
```bash
# Check Python version (requires 3.x)
python3 --version

# If python3 not found, install Python 3
brew install python3  # macOS
```

## 📝 Notes

- **Repository Context**: Run from your dbt repository root for best results
- **Model Selection**: Use Sonnet 4 for best codebase analysis capabilities
- **Cost**: Claude CLI usage counts against your API quota
- **Manual Mode**: Always available as fallback if CLI unavailable

## 🚀 Next Steps

After analysis:
1. Review results with data platform team
2. Validate findings with business stakeholders
3. Share recommendations with Orchestration Services
4. Update sync configurations based on criticality

---

**Version:** 2.0 (Claude CLI Integration)  
**Date:** October 2025  
**Purpose:** Orchestration Services sync decision analysis

