# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ncat \
    libpq-dev \
    pkg-config \
    libcairo2-dev \
    gcc && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script
COPY entrypoint.sh /entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /entrypoint.sh

# Make port 80 available to the world outside this container
EXPOSE 80

# Command to run on container start
CMD ["/entrypoint.sh"]
