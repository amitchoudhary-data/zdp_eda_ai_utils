#!/bin/bash
# SFDC Field Analyzer - Quick Start Script

echo "🚀 SFDC Field Analyzer - Quick Start"
echo "=================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Make scripts executable
chmod +x simple_field_analyzer.py
chmod +x sfdc_field_analyzer_local.py

echo "✅ Scripts made executable"

# Show available options
echo ""
echo "📋 USAGE OPTIONS:"
echo ""
echo "1️⃣  SINGLE REPOSITORY ANALYSIS:"
echo "   cd /path/to/your/dbt/project"
echo "   python3 $(pwd)/simple_field_analyzer.py --fields=\"field1,field2,field3\""
echo ""
echo "2️⃣  MULTI-REPOSITORY ANALYSIS (with config):"
echo "   # First, edit repos_config_example.json with your paths"
echo "   cp repos_config_example.json my_repos.json"
echo "   # Then run analysis"
echo "   python3 $(pwd)/sfdc_field_analyzer_local.py --fields=\"field1,field2\" --repo-config=\"my_repos.json\""
echo ""
echo "3️⃣  MULTI-REPOSITORY ANALYSIS (quick paths):"
echo "   python3 $(pwd)/sfdc_field_analyzer_local.py --fields=\"field1,field2\" --repo-paths=\"/path/repo1,/path/repo2\""
echo ""
echo "📖 Read README_LOCAL_SETUP.md for detailed instructions"
echo ""
echo "🎯 EXAMPLE - Test with sample fields:"
echo "   python3 $(pwd)/simple_field_analyzer.py --fields=\"subscription_model_type,is_price_ramp\" --prompt-only"
echo ""
echo "✅ Setup complete! Files ready in: $(pwd)"
