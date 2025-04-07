#!/bin/bash

# Test Execution Script for Self-Marketing AI Agent
# This script runs the test suite and generates reports

# Set up environment
echo "Setting up test environment..."
mkdir -p ../reports

# Make test scripts executable
chmod +x test_ai_agent.py
chmod +x run_tests.py

# Run basic tests
echo "Running basic tests..."
python3 run_tests.py --all

# Run tests with HTML report
echo "Running tests with HTML report generation..."
python3 run_tests.py --all --html-report

# Run mock tests for CI/CD pipeline
echo "Running mock tests for CI/CD pipeline..."
python3 run_tests.py --all --mock --json-report

# Run specific module tests
echo "Running self-marketing module tests..."
python3 run_tests.py --self-marketing

echo "Running business adaptability module tests..."
python3 run_tests.py --business-adaptability

echo "Running integration tests..."
python3 run_tests.py --integration

echo "All tests completed!"
