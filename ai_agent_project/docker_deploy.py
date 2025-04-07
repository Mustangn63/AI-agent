#!/usr/bin/env python3

"""
Docker Deployment Script for Self-Marketing AI Agent

This script generates Docker and Docker Compose files for containerized deployment
of the Self-Marketing AI Agent.
"""

import os
import argparse
import sys

def create_dockerfile():
    """Create Dockerfile for the AI Agent."""
    dockerfile_content = """FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \\
    build-essential \\
    postgresql-client \\
    nodejs \\
    npm \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Install frontend dependencies and build
WORKDIR /app/frontend
RUN npm install && npm run build

# Return to app directory
WORKDIR /app

# Expose port
EXPOSE 5000

# Set environment variables
ENV PYTHONUNBUFFERED=1 \\
    PYTHONDONTWRITEBYTECODE=1 \\
    FLASK_APP=src/api/app.py \\
    FLASK_ENV=production

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "src.api.wsgi:app"]
"""
    
    with open("Dockerfile", "w") as f:
        f.write(dockerfile_content)
    
    print("Created Dockerfile")

def create_docker_compose():
    """Create docker-compose.yml for the AI Agent."""
    docker_compose_content = """version: '3.8'

services:
  app:
    build: .
    restart: always
    ports:
      - "5000:5000"
    depends_on:
      - db
      - redis
    environment:
      - DATABASE_URL=postgresql://ai_agent_user:ai_agent_password@db:5432/ai_agent_db
      - REDIS_URL=redis://redis:6379/0
      - SECRET_KEY=change_me_in_production
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
      - ./config:/app/config
    networks:
      - ai_agent_network

  db:
    image: postgres:13
    restart: always
    environment:
      - POSTGRES_USER=ai_agent_user
      - POSTGRES_PASSWORD=ai_agent_password
      - POSTGRES_DB=ai_agent_db
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    networks:
      - ai_agent_network

  redis:
    image: redis:6
    restart: always
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"
    networks:
      - ai_agent_network

  nginx:
    image: nginx:latest
    restart: always
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./nginx/ssl:/etc/nginx/ssl
      - ./frontend/build:/usr/share/nginx/html
    depends_on:
      - app
    networks:
      - ai_agent_network

networks:
  ai_agent_network:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
"""
    
    with open("docker-compose.yml", "w") as f:
        f.write(docker_compose_content)
    
    print("Created docker-compose.yml")

def create_nginx_config():
    """Create Nginx configuration for the AI Agent."""
    os.makedirs("nginx/conf.d", exist_ok=True)
    
    nginx_config_content = """server {
    listen 80;
    server_name localhost;

    location / {
        root /usr/share/nginx/html;
        try_files $uri $uri/ /index.html;
    }

    location /api {
        proxy_pass http://app:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
"""
    
    with open("nginx/conf.d/default.conf", "w") as f:
        f.write(nginx_config_content)
    
    print("Created Nginx configuration")

def create_deployment_script():
    """Create deployment script for the AI Agent."""
    deployment_script_content = """#!/bin/bash

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
"""
    
    with open("deploy.sh", "w") as f:
        f.write(deployment_script_content)
    
    os.chmod("deploy.sh", 0o755)
    print("Created deployment script (deploy.sh)")

def create_kubernetes_manifests():
    """Create Kubernetes manifests for the AI Agent."""
    os.makedirs("kubernetes", exist_ok=True)
    
    # Create namespace
    namespace_content = """apiVersion: v1
kind: Namespace
metadata:
  name: ai-agent
"""
    
    with open("kubernetes/namespace.yaml", "w") as f:
        f.write(namespace_content)
    
    # Create deployment
    deployment_content = """apiVersion: apps/v1
kind: Deployment
metadata:
  name: ai-agent
  namespace: ai-agent
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ai-agent
  template:
    metadata:
      labels:
        app: ai-agent
    spec:
      containers:
      - name: ai-agent
        image: ai-agent:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 5000
        env:
        - name: DATABASE_URL
          valueFrom:
            secretKeyRef:
              name: ai-agent-secrets
              key: database-url
        - name: REDIS_URL
          valueFrom:
            secretKeyRef:
              name: ai-agent-secrets
              key: redis-url
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: ai-agent-secrets
              key: secret-key
        resources:
          limits:
            cpu: "1"
            memory: "2Gi"
          requests:
            cpu: "500m"
            memory: "1Gi"
        livenessProbe:
          httpGet:
            path: /api/health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /api/health
            port: 5000
          initialDelaySeconds: 5
          periodSeconds: 5
        volumeMounts:
        - name: config-volume
          mountPath: /app/config
        - name: data-volume
          mountPath: /app/data
      volumes:
      - name: config-volume
        configMap:
          name: ai-agent-config
      - name: data-volume
        persistentVolumeClaim:
          claimName: ai-agent-data-pvc
"""
    
    with open("kubernetes/deployment.yaml", "w") as f:
        f.write(deployment_content)
    
    # Create service
    service_content = """apiVersion: v1
kind: Service
metadata:
  name: ai-agent
  namespace: ai-agent
spec:
  selector:
    app: ai-agent
  ports:
  - port: 80
    targetPort: 5000
  type: ClusterIP
"""
    
    with open("kubernetes/service.yaml", "w") as f:
        f.write(service_content)
    
    # Create ingress
    ingress_content = """apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ai-agent
  namespace: ai-agent
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  rules:
  - host: ai-agent.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: ai-agent
            port:
              number: 80
  tls:
  - hosts:
    - ai-agent.example.com
    secretName: ai-agent-tls
"""
    
    with open("kubernetes/ingress.yaml", "w") as f:
        f.write(ingress_content)
    
    # Create persistent volume claim
    pvc_content = """apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ai-agent-data-pvc
  namespace: ai-agent
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
"""
    
    with open("kubernetes/pvc.yaml", "w") as f:
        f.write(pvc_content)
    
    # Create config map
    configmap_content = """apiVersion: v1
kind: ConfigMap
metadata:
  name: ai-agent-config
  namespace: ai-agent
data:
  config.yaml: |
    # AI Agent Configuration
    api:
      host: 0.0.0.0
      port: 5000
      debug: false
      allowed_origins:
        - https://ai-agent.example.com
    
    models:
      nlp_engine: gpt-4
      context_window: 8192
      temperature: 0.7
    
    logging:
      level: INFO
      file: /app/logs/ai_agent.log
      max_size: 10MB
      backup_count: 5
    
    features:
      self_marketing: true
      business_adaptability: true
      advanced_analytics: true
      multi_language: false
"""
    
    with open("kubernetes/configmap.yaml", "w") as f:
        f.write(configmap_content)
    
    # Create secrets template
    secrets_content = """apiVersion: v1
kind: Secret
metadata:
  name: ai-agent-secrets
  namespace: ai-agent
type: Opaque
stringData:
  database-url: postgresql://user:password@postgres:5432/ai_agent_db
  redis-url: redis://redis:6379/0
  secret-key: change_me_in_production
  api-key: your_api_key_here
"""
    
    with open("kubernetes/secrets.yaml.template", "w") as f:
        f.write(secrets_content)
    
    # Create Kubernetes deployment script
    k8s_script_content = """#!/bin/bash

# Self-Marketing AI Agent Kubernetes Deployment Script

set -e

echo "========================================"
echo "  Self-Marketing AI Agent K8s Deployment"
echo "========================================"
echo

# Check if kubectl is installed
if ! command -v kubectl &> /dev/null; then
    echo "Error: kubectl is not installed. Please install kubectl first."
    exit 1
fi

# Check if connected to a Kubernetes cluster
if ! kubectl cluster-info &> /dev/null; then
    echo "Error: Not connected to a Kubernetes cluster. Please configure kubectl."
    exit 1
fi

# Create secrets file from template
if [ ! -f kubernetes/secrets.yaml ]; then
    echo "Creating secrets file from template..."
    cp kubernetes/secrets.yaml.template kubernetes/secrets.yaml
    echo "Please update the secrets in kubernetes/secrets.yaml before continuing."
    echo "Then run this script again."
    exit 0
fi

# Apply Kubernetes manifests
echo "Creating namespace..."
kubectl apply -f kubernetes/namespace.yaml

echo "Creating secrets..."
kubectl apply -f kubernetes/secrets.yaml

echo "Creating config map..."
kubectl apply -f kubernetes/configmap.yaml

echo "Creating persistent volume claim..."
kubectl apply -f kubernetes/pvc.yaml

echo "Creating deployment..."
kubectl apply -f kubernetes/deployment.yaml

echo "Creating service..."
kubectl apply -f kubernetes/service.yaml

echo "Creating ingress..."
kubectl apply -f kubernetes/ingress.yaml

echo
echo "Deployment completed successfully!"
echo
echo "To check the status of the deployment:"
echo "kubectl get all -n ai-agent"
echo
echo "To view logs:"
echo "kubectl logs -f deployment/ai-agent -n ai-agent"
echo
"""
    
    with open("deploy-k8s.sh", "w") as f:
        f.write(k8s_script_content)
    
    os.chmod("deploy-k8s.sh", 0o755)
    print("Created Kubernetes manifests and deployment script (deploy-k8s.sh)")

def main():
    parser = argparse.ArgumentParser(description='Generate Docker deployment files for the AI Agent.')
    parser.add_argument('--kubernetes', action='store_true', help='Generate Kubernetes manifests')
    args = parser.parse_args()
    
    print("Generating Docker deployment files for the Self-Marketing AI Agent...")
    
    create_dockerfile()
    create_docker_compose()
    create_nginx_config()
    create_deployment_script()
    
    if args.kubernetes:
        create_kubernetes_manifests()
    
    print("\nAll deployment files have been generated successfully!")
    print("\nTo deploy with Docker Compose:")
    print("1. Review and update configuration files")
    print("2. Run: ./deploy.sh")
    
    if args.kubernetes:
        print("\nTo deploy with Kubernetes:")
        print("1. Build and push the Docker image to your registry")
        print("2. Update the image reference in kubernetes/deployment.yaml")
        print("3. Update the host in kubernetes/ingress.yaml")
        print("4. Run: ./deploy-k8s.sh")
    
    print("\nFor more information, refer to the deployment guide: deployment_guide.md")

if __name__ == "__main__":
    main()
