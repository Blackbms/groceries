# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install the dependencies
RUN poetry install --no-root

# Copy the rest of the application code
COPY . /app

# Expose port 5000 for the Flask app
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=groceries/app.py

# Run the Flask app
CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]