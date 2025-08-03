from langchain.tools import tool
import os

@tool
def create_dockerfile(service_name: str, base_image: str) -> str:
    """
    Creates a Dockerfile for a given service.
    'service_name' is the name of the directory to create the Dockerfile in.
    'base_image' is the Python base image to use (e.g., 'python:3.9-slim').
    """
    try:
        # Create a directory for the service if it doesn't already exist
        os.makedirs(service_name, exist_ok=True)
        
        # Define the Dockerfile content
        dockerfile_content = f"""
# Use an official Python runtime as a parent image
FROM {base_image}

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
# This assumes the Dockerfile is in a subdirectory and we copy the app source from the parent.
COPY . /app

# Install any needed packages specified in requirements.txt
# --no-cache-dir reduces the image size.
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py"]
"""
        # Write the content to the Dockerfile
        with open(f"{service_name}/Dockerfile", "w") as f:
            f.write(dockerfile_content)
            
        return f"Successfully created Dockerfile for '{service_name}' in the '{service_name}/' directory."
    except Exception as e:
        return f"Error creating Dockerfile: {e}"