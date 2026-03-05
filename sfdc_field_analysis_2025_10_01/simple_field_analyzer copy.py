#!/usr/bin/env python3
"""
Simple SFDC Field Analysis Helper
Generates structured analysis requests for Claude

Usage:
    python simple_field_analyzer.py --fields="field1,field2,field3"
"""

import argparse
import json
from datetime import datetime
from typing import List

def generate_claude_analysis_prompt(field_names: List[str]) -> str:
    """Generate a structured prompt for Claude analysis"""

    prompt = f"""
# SFDC Field Dependency Analysis Request

**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Fields to Analyze:** {len(field_names)} fields
**Request Type:** Orchestration Services sync decision analysis

## Fields for Analysis:
{chr(10).join(f"- {field}" for field in field_names)}

## Analysis Requirements:

Please analyze each field using the established methodology:

1. **Staging Layer Analysis**
   - Search for field mapping in staging/zuora/ and staging/sfdc/ models
   - Check for column definitions and transformations
   - Document integration patterns

2. **Foundational Layer Analysis**
   - Search foundational/ models for field consumption
   - Focus on recurring revenue and price ramp models
   - Check fact table incorporation patterns
   - Identify dimension table references

3. **Functional Layer Analysis**
   - Search functional/ models for field usage
   - Focus on SFA/MBA reporting models
   - Check digital-led renewal logic dependencies
   - Identify business metrics calculations

4. **Criticality Assessment**
   - 🔴 CRITICAL: Essential for core business processes
   - 🟡 HIGH: Important for analytics and reporting
   - 🟢 MEDIUM: Limited usage, alternative options exist
   - ⚫ UNUSED: No downstream dependencies found

5. **Sync Recommendations**
   - **KEEP current sync**: Critical/High fields with extensive usage
   - **Alternative sync**: Medium fields with limited impact
   - **EOL recommended**: Unused fields safe for removal

## Expected Output:

For each field, provide:
- **Usage Evidence**: Specific models and patterns found
- **Criticality**: Assessment with rationale
- **Recommendation**: Keep/Alternative/EOL with business justification
- **Downstream Impact**: Models and processes affected

## Analysis Focus Areas:
- Price ramp identification logic
- Revenue recognition calculations
- SFA quarterly analysis models
- MBA reporting dependencies
- Digital-led renewal logic

Please use your available tools (codebase_search, grep, read_file) to perform comprehensive analysis.
"""

    return prompt

def save_analysis_template(field_names: List[str], output_file: str):
    """Save analysis template for manual completion"""

    template = {
        "analysis_metadata": {
            "date": datetime.now().isoformat(),
            "fields_count": len(field_names),
            "analyst": "Claude AI",
            "request_type": "Orchestration Services"
        },
        "fields": {}
    }

    for field_name in field_names:
        template["fields"][field_name] = {
            "staging_usage": [],
            "foundational_usage": [],
            "functional_usage": [],
            "criticality": "",
            "recommendation": "",
            "rationale": "",
            "downstream_impact": "",
            "business_justification": ""
        }

    with open(output_file, 'w') as f:
        json.dump(template, f, indent=2)

    print(f"📄 Analysis template saved to: {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Simple SFDC Field Analysis Helper')
    parser.add_argument('--fields', required=True,
                       help='Comma-separated list of fields to analyze')
    parser.add_argument('--output', default='field_analysis_template.json',
                       help='Output template filename')
    parser.add_argument('--prompt-only', action='store_true',
                       help='Only generate Claude prompt (no template file)')

    args = parser.parse_args()

    # Parse field list
    field_names = [field.strip() for field in args.fields.split(',')]

    print(f"📝 SFDC Field Analysis Helper")
    print(f"🎯 Fields: {', '.join(field_names)}")
    print("="*60)

    # Generate Claude prompt
    prompt = generate_claude_analysis_prompt(field_names)

    print("🤖 CLAUDE ANALYSIS PROMPT:")
    print("="*60)
    print(prompt)
    print("="*60)

    if not args.prompt_only:
        # Save analysis template
        save_analysis_template(field_names, args.output)

    print(f"""
💡 NEXT STEPS:

1. **Copy the prompt above** and paste it into your Claude conversation
2. **Claude will automatically analyze** using available tools
3. **Review the results** and validate with business stakeholders
4. **Share with Orchestration Services** team

🚀 This replaces the complex multi-repo system with a simple, working approach!
""")

if __name__ == "__main__":
    main()
