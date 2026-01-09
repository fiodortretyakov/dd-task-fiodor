# DD Agent - Infrastructure as Code Documentation

This repository includes comprehensive IaC configurations to ensure all development environment settings persist across VM restarts.

## 📁 IaC Files Overview

### Dev Container Configuration

- **[.devcontainer/devcontainer.json](.devcontainer/devcontainer.json)** - Main dev container configuration
  - Python 3.12 base image
  - Git and Git LFS features
  - VS Code extensions (Python, Pylint, GitHub Copilot)
  - Environment variables and PYTHONPATH
  - Post-create command automation
  - Git config mounting

- **[.devcontainer/setup.sh](.devcontainer/setup.sh)** - Automated setup script
  - Installs Python dependencies
  - Installs JupyterLab and dev tools
  - Configures Git LFS
  - Creates .env file from template
  - Sets up Python path

- **[.devcontainer/Dockerfile](.devcontainer/Dockerfile)** - Custom container image (optional)
  - Additional system packages
  - Git LFS system configuration
  - Python environment variables

### VS Code Settings

- **[.vscode/settings.json](.vscode/settings.json)** - Workspace settings
  - Python interpreter path
  - Testing configuration (pytest)
  - Editor formatting rules
  - File exclusions

- **[.vscode/extensions.json](.vscode/extensions.json)** - Recommended extensions
  - Python support
  - Code formatting
  - GitHub Copilot

### Python Environment

- **[pyproject.toml](pyproject.toml)** - Project dependencies and metadata
- **[requirements-dev.txt](requirements-dev.txt)** - Development tools
  - JupyterLab + extensions
  - Testing frameworks
  - Code quality tools

### Git Configuration

- **[.gitattributes](.gitattributes)** - Git LFS and line ending rules
- Git LFS tracking for large files (CSV, JSON, YAML)
- Commit signing enabled in local repo

### CI/CD

- **[.github/workflows/devcontainer-build.yml](.github/workflows/devcontainer-build.yml)** - Dev container build validation

## 🚀 What's Automated

When you rebuild or restart the container, the following happens automatically:

1. ✅ Python 3.12 environment with all dependencies
2. ✅ JupyterLab with Git integration
3. ✅ Git LFS configured
4. ✅ VS Code extensions installed
5. ✅ Python path configured
6. ✅ Testing framework ready (pytest)
7. ✅ Git commit signing enabled
8. ✅ .env file created from template

## 📝 Manual Steps After Rebuild

Only two things need manual intervention:

1. **Update `.env` file** with your Azure OpenAI credentials
2. **Configure Git user** (if needed):

   ```bash
   git config --global user.name "Your Name"
   git config --global user.email "your.email@example.com"
   ```

## 🔄 Rebuild Container

To apply these configurations:

1. In VS Code: `Ctrl+Shift+P` → "Dev Containers: Rebuild Container"
2. Or from command line:

   ```bash
   devcontainer up --workspace-folder .
   ```

## 🛠️ Installed Tools

- Python 3.12
- pip, uv package managers
- Git + Git LFS
- pytest (testing)
- JupyterLab (notebooks)
- black, ruff, pylint (code quality)
- All project dependencies from pyproject.toml

## 📦 Python Packages

All packages are installed via:

- Core: `pyproject.toml` dependencies
- Dev: `requirements-dev.txt` tools
- Auto-installed via `setup.sh` post-create command
