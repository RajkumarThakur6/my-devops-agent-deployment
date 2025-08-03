
# Use an official Python runtime as a parent image
FROM python:3.10

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
