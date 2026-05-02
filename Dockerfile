# Use a lightweight Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies (needed for some ML libraries)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker caching
COPY requirements.txt .

# Install Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Create directories for data and models if they don't exist
RUN mkdir -p data models

# The command to run when the container starts:
# 1. Initialize the database
# 2. Train the model
# 3. Start the scheduler
CMD ["sh", "-c", "python src/database.py && python src/train.py && python scheduler.py"]