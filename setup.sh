#!/bin/bash

# Stop script if anything fails
set -e

echo "Creating Conda environment..."
conda env create -f environment.yml

echo "Activating environment..."
conda activate mcp  # or whatever your env is called

echo "Done. You can now run: conda activate mcp"
