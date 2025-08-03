# 📄 FILE: tools/ci_tool.py
# ==============================================================================
from langchain.tools import tool
import os

@tool
def generate_ci_yaml(project_name: str) -> str:
    """
    Generates a GitHub Actions CI workflow file (.github/workflows/ci.yml).
    'project_name' is used for context in the workflow's name.
    """
    try:
        # GitHub Actions workflows must be in the .github/workflows directory
        os.makedirs(".github/workflows", exist_ok=True)
        
        # Define the CI workflow in YAML format
        ci_yaml = f"""
# Name of the GitHub Actions workflow
name: CI Pipeline for {project_name}

# Triggers for the workflow
on:
  push:
    branches: [ "main" ] # Run on pushes to the main branch
  pull_request:
    branches: [ "main" ] # Run on pull requests targeting the main branch

# Jobs to be executed as part of the workflow
jobs:
  build-and-test:
    # The type of runner that the job will run on
    runs-on: ubuntu-latest
    
    steps:
    # Step 1: Check out the repository code
    - uses: actions/checkout@v3

    # Step 2: Set up the specified Python version
    - name: Set up Python 3.9
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'

    # Step 3: Install project dependencies
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt

    # Step 4: Run tests (this is a placeholder)
    - name: Run tests (placeholder)
      run: |
        # In a real project, you would replace this with your actual test command, e.g., pytest
        echo "Running tests for {project_name}..."
        # Example: pytest
"""
        # Write the workflow to the ci.yml file
        with open(".github/workflows/ci.yml", "w") as f:
            f.write(ci_yaml)
            
        return "Successfully created .github/workflows/ci.yml."
    except Exception as e:
        return f"Error generating CI YAML: {e}"