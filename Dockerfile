# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Expose the port on which the Flask app will run
EXPOSE 3000

# Set the environment variables
# Run the Flask app
CMD ["python", "slackbot.py"]