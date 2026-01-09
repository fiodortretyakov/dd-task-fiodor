#!/bin/bash
set -e

echo "🚀 Setting up DD Agent development environment..."

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install --upgrade pip
pip install -e ".[dev]"

# Install additional development tools
echo "🔧 Installing development tools..."
pip install jupyterlab jupyterlab-git ipykernel nbdime black

# Configure Git LFS
echo "🔧 Configuring Git LFS..."
git lfs install

# Configure Git commit signing if not already set
if ! git config --get commit.gpgsign &>/dev/null; then
    echo "🔐 Enabling Git commit signing..."
    git config --local commit.gpgsign true
fi

# Create .env file from example if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please update .env with your Azure OpenAI credentials"
fi

# Set up Python path
export PYTHONPATH="${PYTHONPATH}:${PWD}:${PWD}/src"

echo "✅ Development environment setup complete!"
echo ""
echo "📝 Next steps:"
echo "  1. Update .env with your Azure OpenAI credentials"
echo "  2. Run 'pytest' to verify the installation"
echo "  3. Run 'dd-agent --help' to see available commands"
