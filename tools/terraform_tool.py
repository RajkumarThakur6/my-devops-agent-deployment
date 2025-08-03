from langchain.tools import tool
import os

@tool
def generate_terraform_files(project_name: str, instance_type: str) -> str:
    """
    Generates Terraform configuration files (main.tf) for creating an AWS EC2 instance.
    The 'project_name' will be used as the resource name.
    The 'instance_type' specifies the EC2 instance size (e.g., 't2.micro').
    """
    try:
        # Create a dedicated directory for Terraform files to keep the project clean
        os.makedirs("terraform", exist_ok=True)
        
        # Define the Terraform configuration as a multi-line string
        terraform_config = f'''
# Terraform provider configuration for AWS
provider "aws" {{
  region = "{os.getenv("REGION_NAME", "ap-south-1")}"
}}

# Terraform resource block to define an AWS EC2 instance
resource "aws_instance" "{project_name}" {{
  # Amazon Machine Image (AMI) ID. This one is for Ubuntu 20.04 LTS in ap-south-1.
  # Ensure this AMI is available in your selected AWS region.
  ami           = "ami-0c55b159cbfafe1f0" 
  instance_type = "{instance_type}"

  # Tags are key-value pairs that help in managing and identifying resources.
  tags = {{
    Name = "{project_name}"
    ManagedBy = "LangChainAgent"
  }}
}}
'''
        # Write the configuration to the main.tf file
        with open("terraform/main.tf", "w") as f:
            f.write(terraform_config)
            
        return "Successfully created terraform/main.tf."
    except Exception as e:
        return f"Error generating Terraform file: {e}"
