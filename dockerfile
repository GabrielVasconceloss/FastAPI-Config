# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get -y update --fix-missing && \
    # Installing common packages
    apt-get -y install \
        ncat \
        libpq-dev \
        gcc \
        build-essential \
        vim \
        git \
        bash \
        wget \
        curl \
        unzip \
        tzdata \
        openssl \
        locales \
        libpq-dev \
        uvicorn \
        pkg-config \
        libcurl4-openssl-dev \
        libssl-dev \
        zlib1g \
        zlib1g-dev \
        liblapack-dev && \
    rm -rf /tmp/* /var/cache/apk/* && \
    /usr/bin/localedef -i pt_BR -f UTF-8 pt_BR.UTF-8 && \
    ln -sf /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime && \
    export LANGUAGE=pt_BR.UTF-8 && \
    export LANG=pt_BR.UTF-8 && \
    export LC_ALL=pt_BR.UTF-8

# Upgrade pip to the latest version
RUN python -m pip install --upgrade pip

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Make port 80 available to the world outside this container
EXPOSE 80

# Command to run on container start
CMD ["/app/entrypoint.sh"]

