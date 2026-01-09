# Optional: Use this if you need custom system packages
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install additional system dependencies if needed
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git-lfs \
        vim \
        curl \
        wget \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Configure Git LFS
RUN git lfs install --system

# Set up Python environment
ENV PYTHONPATH="${PYTHONPATH}:/workspaces/${containerWorkspaceFolderBasename}:/workspaces/${containerWorkspaceFolderBasename}/src"
ENV PYTHONUNBUFFERED=1

# Create workspace directory
WORKDIR /workspaces
