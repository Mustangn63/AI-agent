#!/usr/bin/env python3

"""
Test Suite for Self-Marketing AI Agent

This script tests the functionality of the Self-Marketing AI Agent
across different business contexts and scenarios.
"""

import os
import sys
import json
import unittest
from unittest.mock import MagicMock, patch

# Add project root to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import modules to test
try:
    from src.self_marketing.value_proposition_generator import ValuePropositionGenerator
    from src.self_marketing.roi_calculator import ROICalculator
    from src.self_marketing.capability_showcase import CapabilityShowcase
    from src.self_marketing.competitive_differentiator import CompetitiveDifferentiator
    from src.self_marketing.trust_builder import TrustBuilder
    from src.self_marketing.self_marketing_module import SelfMarketingModule
    
    from src.business_adaptability.industry_classifier import IndustryClassifier
    from src.business_adaptability.business_size_analyzer import BusinessSizeAnalyzer
    from src.business_adaptability.role_recognizer import RoleRecognizer
    from src.business_adaptability.business_context_adapter import BusinessContextAdapter
    
    MODULES_IMPORTED = True
except ImportError as e:
    print(f"Warning: Could not import modules: {e}")
    print("Running tests in mock mode")
    MODULES_IMPORTED = False


class MockModule:
    """Mock class for testing when actual modules are not available."""
    def __init__(self, *args, **kwargs):
        pass
    
    def __getattr__(self, name):
        """Return a mock function for any method call."""
        return MagicMock(return_value={})


# Use actual modules if available, otherwise use mocks
if not MODULES_IMPORTED:
    ValuePropositionGenerator = MockModule
    ROICalculator = MockModule
    CapabilityShowcase = MockModule
    CompetitiveDifferentiator = MockModule
    TrustBuilder = MockModule
    SelfMarketingModule = MockModule
    
    IndustryClassifier = MockModule
    BusinessSizeAnalyzer = MockModule
    RoleRecognizer = MockModule
    BusinessContextAdapter = MockModule


class TestValuePropositionGenerator(unittest.TestCase):
    """Test the Value Proposition Generator module."""
    
    def setUp(self):
        """Set up test environment."""
        self.generator = ValuePropositionGenerator()
    
    def test_generate_value_proposition(self):
        """Test generating a single value proposition."""
        industries = ["retail", "healthcare", "finance", "technology", "manufacturing"]
        business_sizes = ["small", "medium", "enterprise"]
        roles = ["executive", "manager", "specialist"]
        
        for industry in industries:
            for size in business_sizes:
                for role in roles:
                    proposition = self.generator.generate_value_proposition(
                        industry=industry,
                        business_size=size,
                        role=role
                    )
                    
                    # Check that a non-empty string is returned
                    self.assertIsInstance(proposition, str)
                    self.assertTrue(len(proposition) > 0)
                    
                    # Print for manual verification
                    print(f"Value Proposition ({industry}, {size}, {role}):")
                    print(proposition)
                    print()
    
    def test_generate_multiple_propositions(self):
        """Test generating multiple value propositions."""
        propositions = self.generator.generate_multiple_propositions(
            industry="retail",
            business_size="medium",
            role="executive",
            count=3
        )
        
        # Check that the correct number of propositions is returned
        self.assertEqual(len(propositions), 3)
        
        # Check that all propositions are non-empty strings
        for prop in propositions:
            self.assertIsInstance(prop, str)
            self.assertTrue(len(prop) > 0)
        
        # Check that propositions are unique
        self.assertEqual(len(set(propositions)), 3)


class TestROICalculator(unittest.TestCase):
    """Test the ROI Calculator module."""
    
    def setUp(self):
        """Set up test environment."""
        self.calculator = ROICalculator()
    
    def test_calculate_roi(self):
        """Test ROI calculation for different business contexts."""
        industries = ["retail", "healthcare", "finance", "technology", "manufacturing"]
        business_sizes = ["small", "medium", "enterprise"]
        
        for industry in industries:
            for size in business_sizes:
                roi_data = self.calculator.calculate_roi(
                    industry=industry,
                    business_size=size,
                    annual_revenue=1000000 if size == "small" else 10000000 if size == "medium" else 100000000,
                    employees_count=20 if size == "small" else 100 if size == "medium" else 1000
                )
                
                # Check that ROI data contains expected fields
                self.assertIn("roi_percentage", roi_data)
                self.assertIn("payback_period", roi_data)
                self.assertIn("annual_savings", roi_data)
                self.assertIn("implementation_cost", roi_data)
                
                # Check that values are reasonable
                self.assertGreater(roi_data["roi_percentage"], 0)
                self.assertGreater(roi_data["payback_period"], 0)
                self.assertGreater(roi_data["annual_savings"], 0)
                self.assertGreater(roi_data["implementation_cost"], 0)
                
                # Print for manual verification
                print(f"ROI Data ({industry}, {size}):")
                print(f"ROI: {roi_data['roi_percentage']}%")
                print(f"Payback Period: {roi_data['payback_period']} months")
                print(f"Annual Savings: ${roi_data['annual_savings']}")
                print(f"Implementation Cost: ${roi_data['implementation_cost']}")
                print()
    
    def test_generate_roi_summary(self):
        """Test generating ROI summary."""
        roi_data = {
            "roi_percentage": 250,
            "payback_period": 4.8,
            "annual_savings": 125000,
            "implementation_cost": 50000,
            "five_year_return": 575000,
            "productivity_improvement": 15,
            "cost_reduction": 12,
            "revenue_increase": 8
        }
        
        summary = self.calculator.generate_roi_summary(roi_data)
        
        # Check that a non-empty string is returned
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) > 0)
        
        # Check that key metrics are included in the summary
        self.assertIn("250%", summary)
        self.assertIn("4.8", summary)
        self.assertIn("$125,000", summary) or self.assertIn("$125000", summary)
        
        # Print for manual verification
        print("ROI Summary:")
        print(summary)
        print()


class TestCapabilityShowcase(unittest.TestCase):
    """Test the Capability Showcase module."""
    
    def setUp(self):
        """Set up test environment."""
        self.showcase = CapabilityShowcase()
    
    def test_get_relevant_capabilities(self):
        """Test retrieving relevant capabilities for different business contexts."""
        industries = ["retail", "healthcare", "finance", "technology", "manufacturing"]
        business_sizes = ["small", "medium", "enterprise"]
        
        for industry in industries:
            for size in business_sizes:
                capabilities = self.showcase.get_relevant_capabilities(
                    industry=industry,
                    business_size=size
                )
                
                # Check that capabilities contain expected categories
                self.assertIn("core_capabilities", capabilities)
                self.assertIn("industry_capabilities", capabilities)
                self.assertIn("size_capabilities", capabilities)
                
                # Check that each category has at least one capability
                self.assertGreater(len(capabilities["core_capabilities"]), 0)
                self.assertGreater(len(capabilities["industry_capabilities"]), 0)
                self.assertGreater(len(capabilities["size_capabilities"]), 0)
                
                # Print for manual verification
                print(f"Capabilities ({industry}, {size}):")
                print(f"Core: {len(capabilities['core_capabilities'])} capabilities")
                print(f"Industry: {len(capabilities['industry_capabilities'])} capabilities")
                print(f"Size: {len(capabilities['size_capabilities'])} capabilities")
                print()
    
    def test_generate_capability_demonstration(self):
        """Test generating capability demonstration."""
        demonstration = self.showcase.generate_capability_demonstration(
            industry="retail",
            business_size="medium",
            specific_interests=["inventory", "customer"]
        )
        
        # Check that a non-empty string is returned
        self.assertIsInstance(demonstration, str)
        self.assertTrue(len(demonstration) > 0)
        
        # Check that specific interests are addressed
        self.assertTrue("inventory" in demonstration.lower())
        self.assertTrue("customer" in demonstration.lower())
        
        # Print for manual verification
        print("Capability Demonstration:")
        print(demonstration[:500] + "...")
        print()


class TestCompetitiveDifferentiator(unittest.TestCase):
    """Test the Competitive Differentiator module."""
    
    def setUp(self):
        """Set up test environment."""
        self.differentiator = CompetitiveDifferentiator()
    
    def test_get_relevant_differentiators(self):
        """Test retrieving relevant differentiators for different business contexts."""
        industries = ["retail", "healthcare", "finance", "technology", "manufacturing"]
        business_sizes = ["small", "medium", "enterprise"]
        comparison_types = ["human", "ai", "all"]
        
        for industry in industries:
            for size in business_sizes:
                for comp_type in comparison_types:
                    differentiators = self.differentiator.get_relevant_differentiators(
                        industry=industry,
                        business_size=size,
                        comparison_type=comp_type
                    )
                    
                    # Check that appropriate categories are included based on comparison type
                    if comp_type in ["human", "all"]:
                        self.assertIn("vs_human_workers", differentiators)
                    
                    if comp_type in ["ai", "all"]:
                        self.assertIn("vs_other_ai_solutions", differentiators)
                    
                    # Industry and business size differentiators should always be included
                    self.assertIn("industry_specific", differentiators)
                    self.assertIn("business_size", differentiators)
                    
                    # Print for manual verification
                    print(f"Differentiators ({industry}, {size}, {comp_type}):")
                    for category, items in differentiators.items():
                        print(f"{category}: {len(items)} items")
                    print()
    
    def test_generate_competitive_comparison(self):
        """Test generating competitive comparison."""
        comparison = self.differentiator.generate_competitive_comparison(
            industry="finance",
            business_size="enterprise",
            comparison_type="all"
        )
        
        # Check that a non-empty string is returned
        self.assertIsInstance(comparison, str)
        self.assertTrue(len(comparison) > 0)
        
        # Check that key sections are included
        self.assertIn("Advantages Over Human-Performed Tasks", comparison)
        self.assertIn("Advantages Over Other AI Solutions", comparison)
        self.assertIn("Finance Industry-Specific Advantages", comparison)
        self.assertIn("Enterprise Business Size Advantages", comparison)
        
        # Print for manual verification
        print("Competitive Comparison:")
        print(comparison[:500] + "...")
        print()


class TestTrustBuilder(unittest.TestCase):
    """Test the Trust Builder module."""
    
    def setUp(self):
        """Set up test environment."""
        self.trust_builder = TrustBuilder()
    
    def test_get_relevant_trust_information(self):
        """Test retrieving relevant trust information for different industries."""
        industries = ["retail", "healthcare", "finance", "technology", "manufacturing"]
        focus_areas = [["security"], ["privacy"], ["ethics"], ["security", "privacy"], None]
        
        for industry in industries:
            for focus in focus_areas:
                trust_info = self.trust_builder.get_relevant_trust_information(
                    industry=industry,
                    focus_areas=focus
                )
                
                # Check that certifications and commitments are always included
                self.assertIn("certifications", trust_info)
                self.assertIn("trust_commitments", trust_info)
                
                # Check that requested focus areas are included
                if focus:
                    for area in focus:
                        self.assertIn(area, trust_info)
                else:
                    # Default focus areas should be included
                    self.assertIn("security", trust_info)
                    self.assertIn("privacy", trust_info)
                    self.assertIn("ethics", trust_info)
                
                # Industry-specific trust info should be included
                self.assertIn("industry_specific", trust_info)
                
                # Print for manual verification
                print(f"Trust Information ({industry}, {focus}):")
                for category, items in trust_info.items():
                    if isinstance(items, list):
                        print(f"{category}: {len(items)} items")
                    else:
                        print(f"{category}: present")
                print()
    
    def test_generate_trust_statement(self):
        """Test generating trust statement."""
        statement = self.trust_builder.generate_trust_statement(
            industry="healthcare",
            focus_areas=["security", "privacy"]
        )
        
        # Check that a non-empty string is returned
        self.assertIsInstance(statement, str)
        self.assertTrue(len(statement) > 0)
        
        # Check that key sections are included
        self.assertIn("Our Commitments to You", statement)
        self.assertIn("Security Measures", statement)
        self.assertIn("Privacy Protections", statement)
        self.assertIn("Healthcare Industry-Specific Protections", statement)
        self.assertIn("Certifications and Compliance", statement)
        
        # Print for manual verification
        print("Trust Statement:")
        print(statement[:500] + "...")
        print()


class TestSelfMarketingModule(unittest.TestCase):
    """Test the Self-Marketing Module integration."""
    
    def setUp(self):
        """Set up test environment."""
        self.marketing = SelfMarketingModule()
    
    def test_generate_marketing_package(self):
        """Test generating a comprehensive marketing package."""
        package = self.marketing.generate_marketing_package(
            industry="technology",
            business_size="medium",
            role="executive",
            annual_revenue=15000000,
            employees_count=150,
            specific_interests=["development", "collaboration"]
        )
        
        # Check that the package contains all expected components
        self.assertIn("business_context", package)
        self.assertIn("value_propositions", package)
        self.assertIn("roi_analysis", package)
        self.assertIn("capability_demonstration", package)
        self.assertIn("competitive_comparison", package)
        self.assertIn("trust_statement", package)
        
        # Check that business context is correct
        self.assertEqual(package["business_context"]["industry"], "technology")
        self.assertEqual(package["business_context"]["business_size"], "medium")
        self.assertEqual(package["business_context"]["role"], "executive")
        
        # Check that value propositions are provided
        self.assertGreater(len(package["value_propositions"]), 0)
        
        # Check that ROI analysis contains summary and data
        self.assertIn("summary", package["roi_analysis"])
        self.assertIn("detailed_data", package["roi_analysis"])
        
        # Print for manual verification
        print("Marketing Package:")
        print(f"Value Propositions: {len(package['value_propositions'])}")
        print(f"ROI Summary: {package['roi_analysis']['summary'][:100]}...")
        print(f"Capability Demo: {package['capability_demonstration'][:100]}...")
        print(f"Competitive Comparison: {package['competitive_comparison'][:100]}...")
        print(f"Trust Statement: {package['trust_statement'][:100]}...")
        print()
    
    def test_generate_elevator_pitch(self):
        """Test generating an elevator pitch."""
        pitch = self.marketing.generate_elevator_pitch(
            industry="retail",
            business_size="small",
            role="manager"
        )
        
        # Check that a non-empty string is returned
        self.assertIsInstance(pitch, str)
        self.assertTrue(len(pitch) > 0)
        
        # Check that key elements are included
        self.assertIn("retail", pitch.lower())
        self.assertIn("small", pitch.lower())
        
        # Print for manual verification
        print("Elevator Pitch:")
        print(pitch)
        print()
    
    def test_generate_detailed_proposal(self):
        """Test generating a detailed business proposal."""
        proposal = self.marketing.generate_detailed_proposal(
            industry="finance",
            business_size="enterprise",
            role="executive",
            company_name="Global Financial Corp",
            annual_revenue=500000000,
            employees_count=2500,
            specific_interests=["risk", "compliance"]
        )
        
        # Check that a non-empty string is returned
        self.assertIsInstance(proposal, str)
        self.assertTrue(len(proposal) > 0)
        
        # Check that key sections are included
        self.assertIn("# AI Agent Implementation Proposal for Global Financial Corp", proposal)
        self.assertIn("## Executive Summary", proposal)
        self.assertIn("## Value Propositions", proposal)
        self.assertIn("## Return on Investment Analysis", proposal)
        self.assertIn("## Capabilities Demonstration", proposal)
        self.assertIn("## Competitive Advantages", proposal)
        self.assertIn("## Trust and Security Considerations", proposal)
        self.assertIn("## Implementation Timeline", proposal)
        self.assertIn("## Next Steps", proposal)
        
        # Check that specific interests are addressed
        self.assertTrue("risk" in proposal.lower())
        self.assertTrue("compliance" in proposal.lower())
        
        # Print for manual verification
        print("Detailed Proposal:")
        print(proposal[:500] + "...")
        print()


class TestIndustryClassifier(unittest.TestCase):
    """Test the Industry Classifier module."""
    
    def setUp(self):
        """Set up test environment."""
        self.classifier = IndustryClassifier()
    
    def test_classify_industry(self):
        """Test classifying industries from business descriptions."""
        test_cases = [
            {
                "description": "We are a retail company selling electronics and home appliances through our chain of stores and e-commerce website.",
                "expected_industry": "retail"
            },
            {
                "description": "Our hospital provides comprehensive healthcare services including emergency care, surgery, and specialized treatments.",
                "expected_industry": "healthcare"
            },
            {
                "description": "We are a financial services firm offering investment management, wealth planning, and banking services to high-net-worth individuals.",
                "expected_industry": "finance"
            },
            {
                "description": "Our software development company creates custom applications and IT solutions for businesses across various industries.",
                "expected_industry": "technology"
            },
            {
                "description": "We manufacture automotive components and parts for major car manufacturers worldwide.",
                "expected_industry": "manufacturing"
            }
        ]
        
        for case in test_cases:
            classification = self.classifier.classify_industry(
                business_description=case["description"]
            )
            
            # Check that classification contains expected fields
            self.assertIn("primary_industry", classification)
            self.assertIn("sub_industry", classification)
            self.assertIn("all_matches", classification)
            
            # Check that the primary industry is correctly identified
            self.assertEqual(classification["primary_industry"]["id"], case["expected_industry"])
            
            # Check that confidence is reasonable
            self.assertGreaterEqual(classification["primary_industry"]["confidence"], 0)
            self.assertLessEqual(classification["primary_industry"]["confidence"], 100)
            
            # Print for manual verification
            print(f"Industry Classification for: {case['description'][:50]}...")
            print(f"Primary Industry: {classification['primary_industry']['name']} (Confidence: {classification['primary_industry']['confidence']}%)")
            if classification['sub_industry']['id']:
                print(f"Sub-Industry: {classification['sub_industry']['name']} (Confidence: {classification['sub_industry']['confidence']}%)")
            print()
    
    def test_get_industry_information(self):
        """Test retrieving detailed industry information."""
        industries = ["retail", "healthcare", "finance", "technology", "manufacturing"]
        
        for industry in industries:
            info = self.classifier.get_industry_information(industry)
            
            # Check that industry information contains expected fields
            self.assertIn("name", info)
            self.assertIn("description", info)
            self.assertIn("keywords", info)
            self.assertIn("sub_industries", info)
            
            # Check that sub-industries are provided
            self.assertGreater(len(info["sub_industries"]), 0)
            
            # Print for manual verification
            print(f"Industry Information for {industry}:")
            print(f"Name: {info['name']}")
            print(f"Description: {info['description']}")
            print(f"Sub-industries: {len(info['sub_industries'])}")
            print()


class TestBusinessSizeAnalyzer(unittest.TestCase):
    """Test the Business Size Analyzer module."""
    
    def setUp(self):
        """Set up test environment."""
        self.analyzer = BusinessSizeAnalyzer()
    
    def test_analyze_business_size(self):
        """Test analyzing business size for different scenarios."""
        test_cases = [
            {
                "industry": "retail",
                "employees": 15,
                "revenue": 2000000,
                "additional": {"locations": 2},
                "expected_size": "small"
            },
            {
                "industry": "retail",
                "employees": 120,
                "revenue": 30000000,
                "additional": {"locations": 12},
                "expected_size": "medium"
            },
            {
                "industry": "healthcare",
                "employees": 600,
                "revenue": 150000000,
                "additional": {"beds": 300},
                "expected_size": "enterprise"
            },
            {
                "industry": "technology",
                "employees": 40,
                "revenue": 8000000,
                "additional": {"users": 50000},
                "expected_size": "small"
            },
            {
                "industry": "finance",
                "employees": 500,
                "revenue": 200000000,
                "additional": {"assets_under_management": 500000000},
                "expected_size": "medium"
            }
        ]
        
        for case in test_cases:
            analysis = self.analyzer.analyze_business_size(
                industry=case["industry"],
                employees_count=case["employees"],
                annual_revenue=case["revenue"],
                additional_metrics=case["additional"]
            )
            
            # Check that analysis contains expected fields
            self.assertIn("size_category", analysis)
            self.assertIn("confidence", analysis)
            self.assertIn("description", analysis)
            self.assertIn("challenges", analysis)
            self.assertIn("opportunities", analysis)
            self.assertIn("metrics_analysis", analysis)
            
            # Check that the size category is correctly identified
            self.assertEqual(analysis["size_category"], case["expected_size"])
            
            # Check that confidence is reasonable
            self.assertGreaterEqual(analysis["confidence"], 0)
            self.assertLessEqual(analysis["confidence"], 100)
            
            # Print for manual verification
            print(f"Business Size Analysis for {case['industry']} (Employees: {case['employees']}, Revenue: ${case['revenue']}):")
            print(f"Size Category: {analysis['size_category'].capitalize()} (Confidence: {analysis['confidence']}%)")
            print(f"Metrics Analysis: {len(analysis['metrics_analysis'])} metrics")
            print()
    
    def test_get_size_information(self):
        """Test retrieving detailed size information."""
        sizes = ["small", "medium", "enterprise"]
        
        for size in sizes:
            info = self.analyzer.get_size_information(size)
            
            # Check that size information contains expected fields
            self.assertIn("description", info)
            self.assertIn("challenges", info)
            self.assertIn("opportunities", info)
            
            # Check that challenges and opportunities are provided
            self.assertGreater(len(info["challenges"]), 0)
            self.assertGreater(len(info["opportunities"]), 0)
            
            # Print for manual verification
            print(f"Size Information for {size}:")
            print(f"Description: {info['description']}")
            print(f"Challenges: {len(info['challenges'])}")
            print(f"Opportunities: {len(info['opportunities'])}")
            print()


class TestRoleRecognizer(unittest.TestCase):
    """Test the Role Recognizer module."""
    
    def setUp(self):
        """Set up test environment."""
        self.recognizer = RoleRecognizer()
    
    def test_recognize_role(self):
        """Test recognizing roles from job titles and additional information."""
        test_cases = [
            {
                "title": "CEO",
                "info": "Responsible for overall company strategy and growth",
                "industry": "technology",
                "expected_org_role": "executive"
            },
            {
                "title": "Marketing Manager",
                "info": "Oversees digital marketing campaigns and team of specialists",
                "industry": "retail",
                "expected_org_role": "manager",
                "expected_func_role": "marketing"
            },
            {
                "title": "Software Developer",
                "info": "Builds web applications using modern frameworks",
                "industry": "technology",
                "expected_org_role": "specialist",
                "expected_func_role": "technology"
            },
            {
                "title": "Chief Financial Officer",
                "info": "Manages financial operations and reporting",
                "industry": "finance",
                "expected_org_role": "executive",
                "expected_func_role": "finance"
            },
            {
                "title": "Nurse Practitioner",
                "info": "Provides patient care and treatment in hospital setting",
                "industry": "healthcare",
                "expected_org_role": "specialist"
            }
        ]
        
        for case in test_cases:
            recognition = self.recognizer.recognize_role(
                job_title=case["title"],
                additional_info=case["info"],
                industry=case["industry"]
            )
            
            # Check that recognition contains expected fields
            self.assertIn("organizational_role", recognition)
            self.assertIn("functional_role", recognition)
            self.assertIn("communication_strategy", recognition)
            self.assertIn("all_matches", recognition)
            
            # Check that the organizational role is correctly identified
            self.assertEqual(recognition["organizational_role"]["id"], case["expected_org_role"])
            
            # Check functional role if expected
            if "expected_func_role" in case:
                self.assertEqual(recognition["functional_role"]["id"], case["expected_func_role"])
            
            # Check that confidence is reasonable
            self.assertGreaterEqual(recognition["organizational_role"]["confidence"], 0)
            self.assertLessEqual(recognition["organizational_role"]["confidence"], 100)
            
            # Print for manual verification
            print(f"Role Recognition for {case['title']} ({case['info']}):")
            print(f"Organizational Role: {recognition['organizational_role']['name']} (Confidence: {recognition['organizational_role']['confidence']}%)")
            print(f"Functional Role: {recognition['functional_role']['name']} (Confidence: {recognition['functional_role']['confidence']}%)")
            if recognition['industry_specific_role']:
                print(f"Industry-Specific Role: {recognition['industry_specific_role']['name']} (Confidence: {recognition['industry_specific_role']['confidence']}%)")
            print()
    
    def test_get_communication_strategy(self):
        """Test retrieving communication strategies for different roles."""
        roles = ["executive", "manager", "specialist"]
        
        for role in roles:
            strategy = self.recognizer.get_communication_strategy(role)
            
            # Check that strategy contains expected fields
            self.assertIn("content_focus", strategy)
            self.assertIn("presentation_style", strategy)
            self.assertIn("language_patterns", strategy)
            
            # Check that strategy components are provided
            self.assertGreater(len(strategy["content_focus"]), 0)
            self.assertGreater(len(strategy["presentation_style"]), 0)
            self.assertGreater(len(strategy["language_patterns"]), 0)
            
            # Print for manual verification
            print(f"Communication Strategy for {role}:")
            print(f"Content Focus: {len(strategy['content_focus'])} items")
            print(f"Presentation Style: {len(strategy['presentation_style'])} items")
            print(f"Language Patterns: {len(strategy['language_patterns'])} items")
            print()


class TestBusinessContextAdapter(unittest.TestCase):
    """Test the Business Context Adapter module."""
    
    def setUp(self):
        """Set up test environment."""
        self.adapter = BusinessContextAdapter()
    
    def test_analyze_business_context(self):
        """Test analyzing comprehensive business context."""
        test_cases = [
            {
                "description": "We are a retail company selling electronics and home appliances through our chain of stores and e-commerce website.",
                "job_title": "Marketing Director",
                "employees": 120,
                "revenue": 25000000,
                "additional_info": {
                    "keywords": ["retail", "electronics", "e-commerce", "omnichannel"],
                    "role_info": "Responsible for digital marketing strategy and brand development",
                    "industry_metrics": {"locations": 8}
                }
            },
            {
                "description": "Our hospital provides comprehensive healthcare services including emergency care, surgery, and specialized treatments.",
                "job_title": "Chief Medical Officer",
                "employees": 800,
                "revenue": 150000000,
                "additional_info": {
                    "keywords": ["healthcare", "hospital", "medical", "patient care"],
                    "role_info": "Oversees medical staff and clinical operations",
                    "industry_metrics": {"beds": 350}
                }
            },
            {
                "description": "We are a small software development company creating custom applications for businesses.",
                "job_title": "Lead Developer",
                "employees": 15,
                "revenue": 2000000,
                "additional_info": {
                    "keywords": ["software", "development", "applications", "programming"],
                    "role_info": "Leads development team and architecture decisions",
                    "industry_metrics": {"users": 5000}
                }
            }
        ]
        
        for case in test_cases:
            context = self.adapter.analyze_business_context(
                business_description=case["description"],
                job_title=case["job_title"],
                employees_count=case["employees"],
                annual_revenue=case["revenue"],
                additional_info=case["additional_info"]
            )
            
            # Check that context contains expected sections
            self.assertIn("industry", context)
            self.assertIn("business_size", context)
            self.assertIn("user_role", context)
            self.assertIn("detailed_analysis", context)
            
            # Check that industry information is provided
            self.assertIn("id", context["industry"])
            self.assertIn("name", context["industry"])
            self.assertIn("confidence", context["industry"])
            
            # Check that business size information is provided
            self.assertIn("category", context["business_size"])
            self.assertIn("confidence", context["business_size"])
            self.assertIn("description", context["business_size"])
            self.assertIn("challenges", context["business_size"])
            self.assertIn("opportunities", context["business_size"])
            
            # Check that user role information is provided
            self.assertIn("organizational", context["user_role"])
            self.assertIn("functional", context["user_role"])
            self.assertIn("communication_strategy", context["user_role"])
            
            # Print for manual verification
            print(f"Business Context Analysis for: {case['description'][:50]}...")
            print(f"Industry: {context['industry']['name']} (Confidence: {context['industry']['confidence']}%)")
            print(f"Business Size: {context['business_size']['category'].capitalize()} (Confidence: {context['business_size']['confidence']}%)")
            print(f"Organizational Role: {context['user_role']['organizational']['name']} (Confidence: {context['user_role']['organizational']['confidence']}%)")
            print(f"Functional Role: {context['user_role']['functional']['name']} (Confidence: {context['user_role']['functional']['confidence']}%)")
            print()
    
    def test_generate_adaptation_strategy(self):
        """Test generating adaptation strategy based on business context."""
        # Create a sample business context
        context = {
            "industry": {
                "id": "retail",
                "name": "Retail",
                "confidence": 85.5,
                "sub_industry": {
                    "id": "electronics",
                    "name": "Electronics and Appliances",
                    "confidence": 75.0
                }
            },
            "business_size": {
                "category": "medium",
                "confidence": 90.0,
                "description": "Medium-sized businesses have more resources than small businesses but still maintain some flexibility.",
                "challenges": ["Growing pains during scaling", "Balancing formality with flexibility"],
                "opportunities": ["Established market presence", "More resources for growth and innovation"]
            },
            "user_role": {
                "organizational": {
                    "id": "executive",
                    "name": "Executive",
                    "confidence": 80.0
                },
                "functional": {
                    "id": "marketing",
                    "name": "Marketing",
                    "confidence": 85.0
                },
                "industry_specific": None,
                "communication_strategy": {
                    "content_focus": ["Strategic impact and business outcomes"],
                    "presentation_style": ["Begin with key conclusions and recommendations"],
                    "language_patterns": ["Strategic, forward-looking terminology"]
                }
            }
        }
        
        strategy = self.adapter.generate_adaptation_strategy(context)
        
        # Check that strategy contains expected sections
        self.assertIn("content_adaptation", strategy)
        self.assertIn("feature_adaptation", strategy)
        self.assertIn("engagement_strategy", strategy)
        
        # Check that content adaptation includes industry focus
        self.assertIn("industry_focus", strategy["content_adaptation"])
        self.assertIn("business_size_adaptation", strategy["content_adaptation"])
        self.assertIn("role_based_communication", strategy["content_adaptation"])
        
        # Check that feature adaptation includes recommended capabilities
        self.assertIn("recommended_capabilities", strategy["feature_adaptation"])
        self.assertIn("interface_customization", strategy["feature_adaptation"])
        self.assertIn("integration_priorities", strategy["feature_adaptation"])
        
        # Check that engagement strategy includes value proposition focus
        self.assertIn("value_proposition_focus", strategy["engagement_strategy"])
        self.assertIn("roi_emphasis", strategy["engagement_strategy"])
        self.assertIn("trust_building_approach", strategy["engagement_strategy"])
        
        # Print for manual verification
        print("Adaptation Strategy:")
        print("Content Adaptation:")
        print(f"- Industry Focus: {len(strategy['content_adaptation']['industry_focus']['primary_topics'])} topics")
        print(f"- Business Size Adaptation: {len(strategy['content_adaptation']['business_size_adaptation']['resource_considerations'])} considerations")
        print(f"- Role-Based Communication: {len(strategy['content_adaptation']['role_based_communication']['content_focus'])} focus areas")
        
        print("\nFeature Adaptation:")
        print(f"- Recommended Capabilities: {len(strategy['feature_adaptation']['recommended_capabilities'])} capabilities")
        print(f"- Interface Customization: {len(strategy['feature_adaptation']['interface_customization'])} customizations")
        print(f"- Integration Priorities: {len(strategy['feature_adaptation']['integration_priorities'])} priorities")
        
        print("\nEngagement Strategy:")
        print(f"- Value Proposition Focus: {len(strategy['engagement_strategy']['value_proposition_focus'])} propositions")
        print(f"- ROI Emphasis: {len(strategy['engagement_strategy']['roi_emphasis'])} emphasis areas")
        print(f"- Trust Building Approach: {len(strategy['engagement_strategy']['trust_building_approach'])} approaches")
        print()


class TestIntegrationScenarios(unittest.TestCase):
    """Test integrated scenarios across multiple modules."""
    
    def setUp(self):
        """Set up test environment."""
        self.business_adapter = BusinessContextAdapter()
        self.marketing_module = SelfMarketingModule()
    
    def test_end_to_end_scenario(self):
        """Test an end-to-end scenario from business context to marketing package."""
        # Test cases representing different business scenarios
        test_cases = [
            {
                "name": "Retail Executive",
                "description": "We are a medium-sized retail chain selling electronics and home appliances with 15 stores across the region and a growing e-commerce presence.",
                "job_title": "Chief Executive Officer",
                "employees": 250,
                "revenue": 45000000,
                "additional_info": {
                    "keywords": ["retail", "electronics", "appliances", "e-commerce", "omnichannel"],
                    "role_info": "Responsible for overall company strategy, growth, and profitability",
                    "industry_metrics": {"locations": 15}
                }
            },
            {
                "name": "Healthcare Manager",
                "description": "Our medical clinic provides primary care services with a team of physicians, nurses, and support staff. We serve approximately 5,000 patients annually.",
                "job_title": "Clinic Manager",
                "employees": 35,
                "revenue": 4500000,
                "additional_info": {
                    "keywords": ["healthcare", "medical", "clinic", "primary care", "patients"],
                    "role_info": "Oversees daily operations, staff scheduling, and patient experience",
                    "industry_metrics": {"beds": 0}
                }
            },
            {
                "name": "Technology Specialist",
                "description": "We develop custom software solutions for businesses in the financial services industry, specializing in data analytics and reporting tools.",
                "job_title": "Senior Developer",
                "employees": 18,
                "revenue": 2800000,
                "additional_info": {
                    "keywords": ["software", "development", "financial services", "data analytics", "custom solutions"],
                    "role_info": "Designs and implements software architecture and leads development team",
                    "industry_metrics": {"users": 2500}
                }
            }
        ]
        
        for case in test_cases:
            print(f"\n{'=' * 80}")
            print(f"TESTING END-TO-END SCENARIO: {case['name']}")
            print(f"{'=' * 80}\n")
            
            # Step 1: Analyze business context
            print("Step 1: Analyzing business context...")
            context = self.business_adapter.analyze_business_context(
                business_description=case["description"],
                job_title=case["job_title"],
                employees_count=case["employees"],
                annual_revenue=case["revenue"],
                additional_info=case["additional_info"]
            )
            
            print(f"Industry: {context['industry']['name']}")
            print(f"Business Size: {context['business_size']['category'].capitalize()}")
            print(f"Organizational Role: {context['user_role']['organizational']['name']}")
            print(f"Functional Role: {context['user_role']['functional']['name']}")
            print()
            
            # Step 2: Generate adaptation strategy
            print("Step 2: Generating adaptation strategy...")
            strategy = self.business_adapter.generate_adaptation_strategy(context)
            
            print("Content Adaptation Strategy:")
            for focus in strategy['content_adaptation']['role_based_communication']['content_focus'][:2]:
                print(f"- {focus}")
            print()
            
            print("Recommended Capabilities:")
            for capability in strategy['feature_adaptation']['recommended_capabilities'][:3]:
                print(f"- {capability}")
            print()
            
            print("Value Proposition Focus:")
            for prop in strategy['engagement_strategy']['value_proposition_focus'][:2]:
                print(f"- {prop}")
            print()
            
            # Step 3: Generate marketing materials
            print("Step 3: Generating marketing materials...")
            
            # Generate elevator pitch
            pitch = self.marketing_module.generate_elevator_pitch(
                industry=context['industry']['id'],
                business_size=context['business_size']['category'],
                role=context['user_role']['organizational']['id']
            )
            
            print("Elevator Pitch:")
            print(pitch)
            print()
            
            # Generate detailed proposal
            proposal = self.marketing_module.generate_detailed_proposal(
                industry=context['industry']['id'],
                business_size=context['business_size']['category'],
                role=context['user_role']['organizational']['id'],
                company_name=f"{case['name']} Company",
                annual_revenue=case["revenue"],
                employees_count=case["employees"]
            )
            
            print("Detailed Proposal (excerpt):")
            print(proposal[:300] + "...")
            print()
            
            # Verify results
            self.assertIsInstance(pitch, str)
            self.assertTrue(len(pitch) > 0)
            self.assertIsInstance(proposal, str)
            self.assertTrue(len(proposal) > 0)
            
            print(f"{'=' * 80}")
            print(f"END-TO-END SCENARIO COMPLETED: {case['name']}")
            print(f"{'=' * 80}\n")


def run_tests():
    """Run the test suite."""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add tests to the suite
    test_suite.addTest(unittest.makeSuite(TestValuePropositionGenerator))
    test_suite.addTest(unittest.makeSuite(TestROICalculator))
    test_suite.addTest(unittest.makeSuite(TestCapabilityShowcase))
    test_suite.addTest(unittest.makeSuite(TestCompetitiveDifferentiator))
    test_suite.addTest(unittest.makeSuite(TestTrustBuilder))
    test_suite.addTest(unittest.makeSuite(TestSelfMarketingModule))
    
    test_suite.addTest(unittest.makeSuite(TestIndustryClassifier))
    test_suite.addTest(unittest.makeSuite(TestBusinessSizeAnalyzer))
    test_suite.addTest(unittest.makeSuite(TestRoleRecognizer))
    test_suite.addTest(unittest.makeSuite(TestBusinessContextAdapter))
    
    test_suite.addTest(unittest.makeSuite(TestIntegrationScenarios))
    
    # Run the tests
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_result = test_runner.run(test_suite)
    
    # Print summary
    print("\nTest Summary:")
    print(f"Ran {test_result.testsRun} tests")
    print(f"Failures: {len(test_result.failures)}")
    print(f"Errors: {len(test_result.errors)}")
    
    return test_result


if __name__ == "__main__":
    print("Running Self-Marketing AI Agent Test Suite")
    print("=" * 50)
    
    if not MODULES_IMPORTED:
        print("\nWARNING: Running in mock mode. Actual modules could not be imported.")
        print("This will test the structure but not the actual functionality.\n")
    
    result = run_tests()
    
    # Exit with appropriate code
    sys.exit(len(result.failures) + len(result.errors))
