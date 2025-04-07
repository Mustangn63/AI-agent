#!/bin/bash

# Self-Marketing AI Agent Docker Deployment Script

set -e

echo "========================================"
echo "  Self-Marketing AI Agent Deployment    "
echo "========================================"
echo

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "Error: Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "Error: Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create required directories
mkdir -p data logs config nginx/ssl

# Copy configuration files if they don't exist
if [ ! -f config/config.yaml ]; then
    echo "Copying default configuration..."
    cp config.example.yaml config/config.yaml
    echo "Please update the configuration in config/config.yaml"
fi

# Build and start the containers
echo "Building and starting containers..."
docker-compose up -d --build

echo
echo "Deployment completed successfully!"
echo
echo "The AI Agent is now running at:"
echo "- Web interface: http://localhost"
echo "- API: http://localhost/api"
echo
echo "To view logs:"
echo "docker-compose logs -f app"
echo
echo "To stop the services:"
echo "docker-compose down"
echo
