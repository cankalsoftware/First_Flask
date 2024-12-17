# Use the official Python image from Docker Hub
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask runs on
EXPOSE 5000

# Define the command to run the Flask app
CMD ["python", "app.py"]
