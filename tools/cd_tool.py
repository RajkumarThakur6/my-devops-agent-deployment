# 📄 FILE: tools/cd_tool.py
# ==============================================================================
from langchain.tools import tool

@tool
def trigger_cd_pipeline(project_name: str) -> str:
    """
    Simulates triggering a Continuous Deployment (CD) pipeline for a given project.
    In a real-world scenario, this would make an API call to a CI/CD server like Jenkins, GitLab, or trigger a GitHub Actions webhook.
    """
    print(f"INFO: Received trigger for CD pipeline for project: {project_name}")
    # This is a simulation. A real implementation would involve HTTP requests, etc.
    return f"CD pipeline for '{project_name}' has been successfully triggered (simulation)."