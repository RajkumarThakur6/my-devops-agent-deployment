from langchain.tools import tool
import os

@tool
def generate_k8s_manifest(service_name: str, image_name: str) -> str:
    """
    Generates a Kubernetes deployment and service YAML file.
    'service_name' is used for naming resources (e.g., 'payment-service').
    'image_name' is the Docker image to be deployed (e.g., 'username/payment-service:v1').
    """
    try:
        # Define the Kubernetes manifest content using a multi-line f-string
        k8s_manifest = f"""
# Kubernetes Deployment configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {service_name}-deployment
  labels:
    app: {service_name}
spec:
  replicas: 2 # Run two pods for high availability
  selector:
    matchLabels:
      app: {service_name}
  template:
    metadata:
      labels:
        app: {service_name}
    spec:
      containers:
      - name: {service_name}-container
        image: {image_name}
        ports:
        - containerPort: 5000 # The port the application listens on inside the container
---
# Kubernetes Service configuration to expose the deployment
apiVersion: v1
kind: Service
metadata:
  name: {service_name}-service
spec:
  # This selector ensures the service routes traffic to pods with the 'app: {service_name}' label
  selector:
    app: {service_name}
  ports:
    - protocol: TCP
      port: 80 # The port the service is exposed on
      targetPort: 5000 # The port to forward traffic to on the pods
  # Exposes the service on an external IP, using the cloud provider's load balancer
  type: LoadBalancer
"""
        # Write the manifest to a YAML file
        with open(f"{service_name}_deployment.yaml", "w") as f:
            f.write(k8s_manifest)
            
        return f"Successfully created {service_name}_deployment.yaml."
    except Exception as e:
        return f"Error generating Kubernetes manifest: {e}"