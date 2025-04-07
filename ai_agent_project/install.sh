#!/bin/bash

# AI Agent Installation Script
# This script automates the installation process for the self-marketing AI agent

# Exit on error
set -e

echo "========================================"
echo "  Self-Marketing AI Agent Installation  "
echo "========================================"
echo

# Check system requirements
echo "Checking system requirements..."
CPU_CORES=$(nproc)
TOTAL_MEM=$(free -m | awk '/^Mem:/{print $2}')
AVAIL_DISK=$(df -h . | awk 'NR==2 {print $4}' | sed 's/G//')

echo "- CPU Cores: $CPU_CORES (minimum: 4)"
echo "- Memory: $TOTAL_MEM MB (minimum: 8192 MB)"
echo "- Available Disk: $AVAIL_DISK GB (minimum: 20 GB)"

if [ $CPU_CORES -lt 4 ]; then
    echo "WARNING: Insufficient CPU cores. Minimum requirement is 4 cores."
fi

if [ $TOTAL_MEM -lt 8192 ]; then
    echo "WARNING: Insufficient memory. Minimum requirement is 8 GB RAM."
fi

if [ ${AVAIL_DISK%.*} -lt 20 ]; then
    echo "WARNING: Insufficient disk space. Minimum requirement is 20 GB available space."
fi

echo

# Check for required software
echo "Checking for required software..."

# Check Python version
if command -v python3 &>/dev/null; then
    PYTHON_VERSION=$(python3 --version | awk '{print $2}')
    echo "- Python version: $PYTHON_VERSION"
    
    # Compare version
    PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
    PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)
    
    if [ $PYTHON_MAJOR -lt 3 ] || ([ $PYTHON_MAJOR -eq 3 ] && [ $PYTHON_MINOR -lt 8 ]); then
        echo "  WARNING: Python 3.8+ is required."
    fi
else
    echo "  WARNING: Python 3 not found. Please install Python 3.8 or higher."
fi

# Check Node.js version
if command -v node &>/dev/null; then
    NODE_VERSION=$(node --version | cut -c 2-)
    echo "- Node.js version: $NODE_VERSION"
    
    # Compare version
    NODE_MAJOR=$(echo $NODE_VERSION | cut -d. -f1)
    
    if [ $NODE_MAJOR -lt 14 ]; then
        echo "  WARNING: Node.js 14+ is required."
    fi
else
    echo "  WARNING: Node.js not found. Please install Node.js 14 or higher."
fi

# Check Docker version
if command -v docker &>/dev/null; then
    DOCKER_VERSION=$(docker --version | awk '{print $3}' | sed 's/,//')
    echo "- Docker version: $DOCKER_VERSION"
else
    echo "  WARNING: Docker not found. Docker is recommended for containerized deployment."
fi

# Check PostgreSQL version
if command -v psql &>/dev/null; then
    PG_VERSION=$(psql --version | awk '{print $3}')
    echo "- PostgreSQL version: $PG_VERSION"
    
    # Compare version
    PG_MAJOR=$(echo $PG_VERSION | cut -d. -f1)
    
    if [ $PG_MAJOR -lt 13 ]; then
        echo "  WARNING: PostgreSQL 13+ is recommended."
    fi
else
    echo "  WARNING: PostgreSQL not found. PostgreSQL 13+ is recommended for data storage."
fi

echo

# Create installation directory
INSTALL_DIR="ai_agent_installation"
echo "Creating installation directory: $INSTALL_DIR"
mkdir -p $INSTALL_DIR
cd $INSTALL_DIR

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip
pip install numpy pandas scikit-learn tensorflow transformers flask sqlalchemy psycopg2-binary pyyaml requests

# Create project structure
echo "Creating project structure..."
mkdir -p src/{core,self_marketing,business_adaptability,api,ui}
mkdir -p config
mkdir -p data
mkdir -p docs
mkdir -p scripts
mkdir -p tests
mkdir -p frontend

# Copy source files
echo "Copying source files..."
# This would normally copy from the installation package
# For this example, we'll create placeholder files

# Create configuration files
echo "Creating configuration files..."
cat > config/config.yaml << EOF
# AI Agent Configuration

# Database settings
database:
  type: postgresql
  host: localhost
  port: 5432
  name: ai_agent_db
  user: ai_agent_user
  password: change_me_immediately

# API settings
api:
  host: 0.0.0.0
  port: 5000
  debug: false
  secret_key: change_me_immediately
  allowed_origins:
    - http://localhost:3000
    - https://yourdomain.com

# AI model settings
models:
  nlp_engine: gpt-4
  context_window: 8192
  temperature: 0.7
  api_key: your_api_key_here

# Logging settings
logging:
  level: INFO
  file: logs/ai_agent.log
  max_size: 10MB
  backup_count: 5

# Security settings
security:
  encryption_key: change_me_immediately
  session_timeout: 3600
  password_min_length: 12
  require_mfa: false

# Feature toggles
features:
  self_marketing: true
  business_adaptability: true
  advanced_analytics: true
  multi_language: false
EOF

# Create initialization script
echo "Creating initialization script..."
cat > scripts/initialize.py << EOF
#!/usr/bin/env python3
"""
Initialization script for the AI Agent.
"""
import os
import sys
import yaml
import argparse
import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger('initializer')

def load_config(config_path):
    """Load configuration from YAML file."""
    logger.info(f"Loading configuration from {config_path}")
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        sys.exit(1)

def setup_database(config):
    """Set up the database."""
    logger.info("Setting up database...")
    # This would normally create the database and tables
    logger.info("Database setup complete.")

def initialize_models(config):
    """Initialize AI models."""
    logger.info("Initializing AI models...")
    # This would normally download and initialize models
    logger.info("AI models initialized.")

def create_admin_user(config, username, email, password):
    """Create an administrator user."""
    logger.info(f"Creating admin user: {username}")
    # This would normally create an admin user
    logger.info("Admin user created successfully.")

def main():
    parser = argparse.ArgumentParser(description='Initialize the AI Agent.')
    parser.add_argument('--config', default='config/config.yaml', help='Path to configuration file')
    parser.add_argument('--admin-username', default='admin', help='Admin username')
    parser.add_argument('--admin-email', default='admin@example.com', help='Admin email')
    parser.add_argument('--admin-password', default=None, help='Admin password')
    args = parser.parse_args()
    
    config = load_config(args.config)
    
    setup_database(config)
    initialize_models(config)
    
    if args.admin_password:
        create_admin_user(config, args.admin_username, args.admin_email, args.admin_password)
    
    logger.info("Initialization complete!")

if __name__ == '__main__':
    logger = setup_logging()
    main()
EOF

chmod +x scripts/initialize.py

# Create README file
echo "Creating README file..."
cat > README.md << EOF
# Self-Marketing AI Agent

An AI agent that can sell itself for any kind of business.

## Features

- Self-marketing capabilities
- Business adaptability features
- Customizable user interface
- Flexible deployment options

## Installation

See the [Deployment Guide](deployment_guide.md) for detailed installation instructions.

## Quick Start

1. Create and activate a virtual environment:
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\\Scripts\\activate
   \`\`\`

2. Install dependencies:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

3. Initialize the system:
   \`\`\`bash
   python scripts/initialize.py --admin-password your_secure_password
   \`\`\`

4. Start the server:
   \`\`\`bash
   python scripts/run_server.py
   \`\`\`

5. Access the web interface at http://localhost:5000

## Documentation

- [User Guide](docs/user_guide.md)
- [API Documentation](docs/api_docs.md)
- [Developer Guide](docs/developer_guide.md)

## Support

For support, please contact support@ai-agent-project.com or visit our community forum.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
EOF

# Create requirements.txt
echo "Creating requirements.txt..."
cat > requirements.txt << EOF
# Core dependencies
numpy>=1.20.0
pandas>=1.3.0
scikit-learn>=1.0.0
tensorflow>=2.8.0
transformers>=4.18.0

# Web framework
flask>=2.0.0
flask-restful>=0.3.9
flask-cors>=3.0.10
gunicorn>=20.1.0

# Database
sqlalchemy>=1.4.0
psycopg2-binary>=2.9.0
alembic>=1.7.0

# Utilities
pyyaml>=6.0
requests>=2.27.0
python-dotenv>=0.20.0
tqdm>=4.64.0

# Testing
pytest>=7.0.0
pytest-cov>=3.0.0

# Documentation
sphinx>=4.5.0
sphinx-rtd-theme>=1.0.0
EOF

# Create run script
echo "Creating run script..."
cat > scripts/run_server.py << EOF
#!/usr/bin/env python3
"""
Run the AI Agent server.
"""
import os
import sys
import yaml
import argparse
import logging

def setup_logging():
    """Set up logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )
    return logging.getLogger('server')

def load_config(config_path):
    """Load configuration from YAML file."""
    logger.info(f"Loading configuration from {config_path}")
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load configuration: {e}")
        sys.exit(1)

def start_server(config):
    """Start the server."""
    logger.info("Starting server...")
    # This would normally start the Flask server
    host = config['api']['host']
    port = config['api']['port']
    logger.info(f"Server running at http://{host}:{port}")
    
    # Placeholder for server startup
    logger.info("Server started successfully.")
    logger.info("Press Ctrl+C to stop the server.")
    
    try:
        # Keep the script running
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("Server stopped.")

def main():
    parser = argparse.ArgumentParser(description='Run the AI Agent server.')
    parser.add_argument('--config', default='config/config.yaml', help='Path to configuration file')
    args = parser.parse_args()
    
    config = load_config(args.config)
    start_server(config)

if __name__ == '__main__':
    logger = setup_logging()
    main()
EOF

chmod +x scripts/run_server.py

echo
echo "Installation files created successfully!"
echo
echo "Next steps:"
echo "1. Review and modify the configuration in config/config.yaml"
echo "2. Initialize the system: python scripts/initialize.py --admin-password your_secure_password"
echo "3. Start the server: python scripts/run_server.py"
echo "4. Access the web interface at http://localhost:5000"
echo
echo "For detailed instructions, refer to the deployment guide: deployment_guide.md"
echo
echo "Installation directory: $(pwd)"
echo
