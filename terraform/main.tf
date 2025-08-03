
# Terraform provider configuration for AWS
provider "aws" {
  region = "ap-south-1"
}

# Terraform resource block to define an AWS EC2 instance
resource "aws_instance" "my-new-app" {
  # Amazon Machine Image (AMI) ID. This one is for Ubuntu 20.04 LTS in ap-south-1.
  # Ensure this AMI is available in your selected AWS region.
  ami           = "ami-0c55b159cbfafe1f0" 
  instance_type = "t3.micro"

  # Tags are key-value pairs that help in managing and identifying resources.
  tags = {
    Name = "my-new-app"
    ManagedBy = "LangChainAgent"
  }
}
