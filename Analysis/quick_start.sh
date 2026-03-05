#!/bin/bash
# Quick Start Script for Atlassian Integration

echo "🚀 Atlassian Integration Quick Start"
echo "===================================="
echo ""

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed"
    echo "   Install from: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python 3 found: $(python3 --version)"

# Check if pip is available
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed"
    exit 1
fi

echo "✅ pip3 found"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
pip3 install -q requests python-dotenv

if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully"
else
    echo "❌ Failed to install dependencies"
    exit 1
fi

echo ""

# Check if .env exists
if [ -f ".env" ]; then
    echo "✅ .env file found"
    echo ""
    echo "Testing connection..."
    python3 atlassian_config.py --test
else
    echo "⚠️  No .env file found"
    echo ""
    echo "Would you like to run the setup wizard? (y/n)"
    read -r response
    
    if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
        python3 atlassian_config.py --setup
    else
        echo ""
        echo "📝 Manual setup:"
        echo "   1. Copy env_template.txt to .env"
        echo "   2. Fill in your Atlassian credentials"
        echo "   3. Run: python3 atlassian_config.py --test"
    fi
fi

echo ""
echo "🎉 Setup complete!"
echo ""
echo "📚 Next steps:"
echo "   • Read ATLASSIAN_SETUP.md for detailed docs"
echo "   • Try: python3 atlassian_config.py --get-issue PROJ-123"
echo "   • Try: python3 atlassian_config.py --search 'project = PROJ'"
echo ""

