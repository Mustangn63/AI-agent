#!/usr/bin/env python3

"""
Test Runner for Self-Marketing AI Agent

This script runs the test suite for the Self-Marketing AI Agent
and generates a detailed test report.
"""

import os
import sys
import time
import datetime
import unittest
import json
import argparse
from unittest.mock import patch

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import test module
from test_ai_agent import (
    TestValuePropositionGenerator,
    TestROICalculator,
    TestCapabilityShowcase,
    TestCompetitiveDifferentiator,
    TestTrustBuilder,
    TestSelfMarketingModule,
    TestIndustryClassifier,
    TestBusinessSizeAnalyzer,
    TestRoleRecognizer,
    TestBusinessContextAdapter,
    TestIntegrationScenarios
)

def generate_html_report(test_results, start_time, end_time):
    """Generate an HTML test report."""
    duration = end_time - start_time
    
    # Create report directory
    os.makedirs("../reports", exist_ok=True)
    
    # Generate timestamp for filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = f"../reports/test_report_{timestamp}.html"
    
    # Calculate statistics
    total_tests = test_results['testsRun']
    passed_tests = total_tests - len(test_results['failures']) - len(test_results['errors'])
    pass_percentage = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    
    # Generate HTML content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Self-Marketing AI Agent Test Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}
        header {{
            background-color: #f8f9fa;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
            border-left: 5px solid #007bff;
        }}
        h1, h2, h3 {{
            color: #007bff;
        }}
        .summary {{
            display: flex;
            justify-content: space-between;
            flex-wrap: wrap;
            margin-bottom: 20px;
        }}
        .summary-card {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 10px;
            flex: 1;
            min-width: 200px;
            margin-right: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .summary-card h3 {{
            margin-top: 0;
        }}
        .progress-bar {{
            height: 20px;
            background-color: #e9ecef;
            border-radius: 5px;
            margin-bottom: 10px;
            overflow: hidden;
        }}
        .progress {{
            height: 100%;
            background-color: #28a745;
            border-radius: 5px;
            width: {pass_percentage}%;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 20px;
        }}
        th, td {{
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        th {{
            background-color: #f8f9fa;
            font-weight: bold;
        }}
        tr:hover {{
            background-color: #f8f9fa;
        }}
        .success {{
            color: #28a745;
        }}
        .failure {{
            color: #dc3545;
        }}
        .error {{
            color: #dc3545;
            font-weight: bold;
        }}
        .details {{
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            margin-top: 10px;
            white-space: pre-wrap;
            font-family: monospace;
            font-size: 14px;
            overflow-x: auto;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Self-Marketing AI Agent Test Report</h1>
            <p>Generated on {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </header>
        
        <div class="summary">
            <div class="summary-card">
                <h3>Test Summary</h3>
                <div class="progress-bar">
                    <div class="progress"></div>
                </div>
                <p><strong>Pass Rate:</strong> {pass_percentage:.2f}%</p>
                <p><strong>Total Tests:</strong> {total_tests}</p>
                <p><strong>Passed:</strong> <span class="success">{passed_tests}</span></p>
                <p><strong>Failed:</strong> <span class="failure">{len(test_results['failures'])}</span></p>
                <p><strong>Errors:</strong> <span class="error">{len(test_results['errors'])}</span></p>
            </div>
            
            <div class="summary-card">
                <h3>Execution Details</h3>
                <p><strong>Start Time:</strong> {datetime.datetime.fromtimestamp(start_time).strftime("%Y-%m-%d %H:%M:%S")}</p>
                <p><strong>End Time:</strong> {datetime.datetime.fromtimestamp(end_time).strftime("%Y-%m-%d %H:%M:%S")}</p>
                <p><strong>Duration:</strong> {duration:.2f} seconds</p>
                <p><strong>Python Version:</strong> {sys.version.split()[0]}</p>
                <p><strong>Platform:</strong> {sys.platform}</p>
            </div>
        </div>
        
        <h2>Test Results</h2>
"""
    
    # Add test class results
    for test_class, results in test_results['results_by_class'].items():
        passed = results['total'] - results['failures'] - results['errors']
        class_pass_percentage = (passed / results['total']) * 100 if results['total'] > 0 else 0
        
        html_content += f"""
        <h3>{test_class}</h3>
        <div class="progress-bar">
            <div class="progress" style="width: {class_pass_percentage}%;"></div>
        </div>
        <p><strong>Pass Rate:</strong> {class_pass_percentage:.2f}%</p>
        <p><strong>Total Tests:</strong> {results['total']} | <strong>Passed:</strong> <span class="success">{passed}</span> | <strong>Failed:</strong> <span class="failure">{results['failures']}</span> | <strong>Errors:</strong> <span class="error">{results['errors']}</span></p>
        
        <table>
            <thead>
                <tr>
                    <th>Test Method</th>
                    <th>Status</th>
                    <th>Duration (s)</th>
                </tr>
            </thead>
            <tbody>
"""
        
        for test_name, test_result in results['tests'].items():
            status_class = "success" if test_result['status'] == 'pass' else "failure" if test_result['status'] == 'fail' else "error"
            status_text = "PASS" if test_result['status'] == 'pass' else "FAIL" if test_result['status'] == 'fail' else "ERROR"
            
            html_content += f"""
                <tr>
                    <td>{test_name}</td>
                    <td class="{status_class}">{status_text}</td>
                    <td>{test_result['duration']:.4f}</td>
                </tr>
"""
            
            if test_result['status'] != 'pass' and 'details' in test_result:
                html_content += f"""
                <tr>
                    <td colspan="3">
                        <div class="details">{test_result['details']}</div>
                    </td>
                </tr>
"""
        
        html_content += """
            </tbody>
        </table>
"""
    
    # Add failures and errors section if any
    if test_results['failures'] or test_results['errors']:
        html_content += """
        <h2>Failures and Errors</h2>
        <table>
            <thead>
                <tr>
                    <th>Test</th>
                    <th>Type</th>
                    <th>Details</th>
                </tr>
            </thead>
            <tbody>
"""
        
        for failure in test_results['failures']:
            html_content += f"""
                <tr>
                    <td>{failure['test']}</td>
                    <td class="failure">Failure</td>
                    <td>
                        <div class="details">{failure['details']}</div>
                    </td>
                </tr>
"""
        
        for error in test_results['errors']:
            html_content += f"""
                <tr>
                    <td>{error['test']}</td>
                    <td class="error">Error</td>
                    <td>
                        <div class="details">{error['details']}</div>
                    </td>
                </tr>
"""
        
        html_content += """
            </tbody>
        </table>
"""
    
    # Close HTML
    html_content += """
    </div>
</body>
</html>
"""
    
    # Write to file
    with open(report_file, 'w') as f:
        f.write(html_content)
    
    return report_file

class CustomTestResult(unittest.TestResult):
    """Custom test result class to capture detailed test information."""
    
    def __init__(self):
        super().__init__()
        self.testsRun = 0
        self.successes = []
        self.failures = []
        self.errors = []
        self.results_by_class = {}
        self.current_test = None
        self.current_test_start_time = None
    
    def startTest(self, test):
        super().startTest(test)
        self.current_test = test
        self.current_test_start_time = time.time()
        
        # Initialize test class results if not exists
        test_class = test.__class__.__name__
        if test_class not in self.results_by_class:
            self.results_by_class[test_class] = {
                'total': 0,
                'failures': 0,
                'errors': 0,
                'tests': {}
            }
    
    def addSuccess(self, test):
        super().addSuccess(test)
        self.successes.append(test)
        
        # Record test result
        test_class = test.__class__.__name__
        test_name = test._testMethodName
        duration = time.time() - self.current_test_start_time
        
        self.results_by_class[test_class]['total'] += 1
        self.results_by_class[test_class]['tests'][test_name] = {
            'status': 'pass',
            'duration': duration
        }
    
    def addFailure(self, test, err):
        super().addFailure(test, err)
        
        # Record test result
        test_class = test.__class__.__name__
        test_name = test._testMethodName
        duration = time.time() - self.current_test_start_time
        
        self.results_by_class[test_class]['total'] += 1
        self.results_by_class[test_class]['failures'] += 1
        self.results_by_class[test_class]['tests'][test_name] = {
            'status': 'fail',
            'duration': duration,
            'details': self._exc_info_to_string(err, test)
        }
        
        self.failures.append({
            'test': f"{test_class}.{test_name}",
            'details': self._exc_info_to_string(err, test)
        })
    
    def addError(self, test, err):
        super().addError(test, err)
        
        # Record test result
        test_class = test.__class__.__name__
        test_name = test._testMethodName
        duration = time.time() - self.current_test_start_time
        
        self.results_by_class[test_class]['total'] += 1
        self.results_by_class[test_class]['errors'] += 1
        self.results_by_class[test_class]['tests'][test_name] = {
            'status': 'error',
            'duration': duration,
            'details': self._exc_info_to_string(err, test)
        }
        
        self.errors.append({
            'test': f"{test_class}.{test_name}",
            'details': self._exc_info_to_string(err, test)
        })

def run_tests(args):
    """Run the test suite with detailed reporting."""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add tests to the suite based on options
    if args.all or args.self_marketing:
        test_suite.addTest(unittest.makeSuite(TestValuePropositionGenerator))
        test_suite.addTest(unittest.makeSuite(TestROICalculator))
        test_suite.addTest(unittest.makeSuite(TestCapabilityShowcase))
        test_suite.addTest(unittest.makeSuite(TestCompetitiveDifferentiator))
        test_suite.addTest(unittest.makeSuite(TestTrustBuilder))
        test_suite.addTest(unittest.makeSuite(TestSelfMarketingModule))
    
    if args.all or args.business_adaptability:
        test_suite.addTest(unittest.makeSuite(TestIndustryClassifier))
        test_suite.addTest(unittest.makeSuite(TestBusinessSizeAnalyzer))
        test_suite.addTest(unittest.makeSuite(TestRoleRecognizer))
        test_suite.addTest(unittest.makeSuite(TestBusinessContextAdapter))
    
    if args.all or args.integration:
        test_suite.addTest(unittest.makeSuite(TestIntegrationScenarios))
    
    # Create custom test result
    test_result = CustomTestResult()
    
    # Run the tests
    start_time = time.time()
    test_suite.run(test_result)
    end_time = time.time()
    
    # Print summary
    print("\nTest Summary:")
    print(f"Ran {test_result.testsRun} tests")
    print(f"Successes: {len(test_result.successes)}")
    print(f"Failures: {len(test_result.failures)}")
    print(f"Errors: {len(test_result.errors)}")
    print(f"Duration: {end_time - start_time:.2f} seconds")
    
    # Generate reports
    if args.html_report:
        report_file = generate_html_report(test_result, start_time, end_time)
        print(f"\nHTML report generated: {report_file}")
    
    if args.json_report:
        # Create report directory
        os.makedirs("../reports", exist_ok=True)
        
        # Generate timestamp for filename
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        json_file = f"../reports/test_report_{timestamp}.json"
        
        # Convert test result to JSON-serializable format
        json_result = {
            'testsRun': test_result.testsRun,
            'successes': len(test_result.successes),
            'failures': len(test_result.failures),
            'errors': len(test_result.errors),
            'duration': end_time - start_time,
            'start_time': start_time,
            'end_time': end_time,
            'results_by_class': test_result.results_by_class,
            'failures': test_result.failures,
            'errors': test_result.errors
        }
        
        # Write to file
        with open(json_file, 'w') as f:
            json.dump(json_result, f, indent=2)
        
        print(f"JSON report generated: {json_file}")
    
    return test_result

def main():
    """Main function to parse arguments and run tests."""
    parser = argparse.ArgumentParser(description='Run tests for the Self-Marketing AI Agent.')
    
    # Test selection options
    test_group = parser.add_argument_group('Test Selection')
    test_group.add_argument('--all', action='store_true', help='Run all tests (default)')
    test_group.add_argument('--self-marketing', action='store_true', help='Run only self-marketing module tests')
    test_group.add_argument('--business-adaptability', action='store_true', help='Run only business adaptability module tests')
    test_group.add_argument('--integration', action='store_true', help='Run only integration tests')
    
    # Report options
    report_group = parser.add_argument_group('Reporting')
    report_group.add_argument('--html-report', action='store_true', help='Generate HTML test report')
    report_group.add_argument('--json-report', action='store_true', help='Generate JSON test report')
    
    # Mock options
    mock_group = parser.add_argument_group('Mocking')
    mock_group.add_argument('--mock', action='store_true', help='Run tests with mock objects instead of actual implementations')
    
    args = parser.parse_args()
    
    # If no test selection is specified, run all tests
    if not (args.all or args.self_marketing or args.business_adaptability or args.integration):
        args.all = True
    
    # If mock mode is requested, patch the modules
    if args.mock:
        print("Running tests in mock mode. Using mock objects instead of actual implementations.")
        
        # Create a context manager that patches all modules
        patch_context = patch.multiple(
            'test_ai_agent',
            MODULES_IMPORTED=False,
            ValuePropositionGenerator=None,
            ROICalculator=None,
            CapabilityShowcase=None,
            CompetitiveDifferentiator=None,
            TrustBuilder=None,
            SelfMarketingModule=None,
            IndustryClassifier=None,
            BusinessSizeAnalyzer=None,
            RoleRecognizer=None,
            BusinessContextAdapter=None
        )
        
        # Run tests with patched modules
        with patch_context:
            result = run_tests(args)
    else:
        # Run tests normally
        result = run_tests(args)
    
    # Return appropriate exit code
    return len(result.failures) + len(result.errors)

if __name__ == "__main__":
    print("Self-Marketing AI Agent Test Runner")
    print("=" * 50)
    
    exit_code = main()
    sys.exit(exit_code)
