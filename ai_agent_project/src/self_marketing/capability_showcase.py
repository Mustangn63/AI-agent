"""
Capability Showcase Module

This module demonstrates relevant capabilities of the AI agent based on 
business needs and interests.
"""

import json
import random
from typing import Dict, List, Optional

class CapabilityShowcase:
    """
    Demonstrates relevant capabilities of the AI agent based on business context.
    """
    
    def __init__(self, capabilities_data_path: str = "capabilities.json"):
        """
        Initialize the Capability Showcase.
        
        Args:
            capabilities_data_path: Path to the capabilities data file
        """
        self.capabilities_data_path = capabilities_data_path
        self.capabilities_data = self._load_capabilities_data()
        
    def _load_capabilities_data(self) -> Dict:
        """
        Load the capabilities data from file.
        
        Returns:
            Dict: The capabilities data
        """
        try:
            with open(self.capabilities_data_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default capabilities data if file not found or invalid
            return self._create_default_capabilities_data()
    
    def _create_default_capabilities_data(self) -> Dict:
        """
        Create default capabilities data with demonstrations for different business contexts.
        
        Returns:
            Dict: Default capabilities data
        """
        default_capabilities = {
            "core_capabilities": {
                "natural_language_processing": {
                    "name": "Natural Language Processing",
                    "description": "Understanding and generating human language naturally",
                    "demo_script": "User: 'I need to analyze customer feedback from our latest product launch.'\nAI: 'I can help with that. I'll analyze sentiment, extract key themes, and identify actionable insights from your customer feedback data.'",
                    "business_value": "Enables efficient processing of text data, customer communications, and content creation."
                },
                "adaptive_learning": {
                    "name": "Adaptive Learning",
                    "description": "Learning from interactions and improving over time",
                    "demo_script": "User: 'How do you improve your performance?'\nAI: 'I continuously learn from our interactions. For example, I've noticed you frequently ask about sales data, so I've prioritized that information in my responses.'",
                    "business_value": "Provides increasingly personalized and relevant assistance as usage continues."
                },
                "decision_support": {
                    "name": "Decision Support",
                    "description": "Providing data-driven recommendations",
                    "demo_script": "User: 'Should we expand our product line or focus on improving existing products?'\nAI: 'Based on your sales data and market trends, I recommend focusing on improving your top three products, which account for 80% of your revenue.'",
                    "business_value": "Helps make informed decisions based on data analysis and business context."
                },
                "process_automation": {
                    "name": "Process Automation",
                    "description": "Automating repetitive tasks and workflows",
                    "demo_script": "User: 'I spend hours each week generating sales reports.'\nAI: 'I can automate that for you. I'll generate weekly sales reports with key metrics and send them to your team every Monday morning.'",
                    "business_value": "Saves time and reduces errors by automating routine tasks."
                },
                "integration_capabilities": {
                    "name": "System Integration",
                    "description": "Connecting with existing business systems",
                    "demo_script": "User: 'Can you work with our CRM system?'\nAI: 'Yes, I can integrate with your CRM to access customer data, update records, and trigger workflows based on customer interactions.'",
                    "business_value": "Works seamlessly with existing tools and systems, maximizing the value of current investments."
                }
            },
            "industry_specific_capabilities": {
                "retail": [
                    {
                        "name": "Inventory Optimization",
                        "description": "Predicting optimal inventory levels",
                        "demo_script": "User: 'We often have too much or too little inventory.'\nAI: 'I can analyze your sales patterns, seasonality, and market trends to recommend optimal inventory levels, reducing both stockouts and excess inventory.'",
                        "business_value": "Reduces carrying costs while ensuring product availability."
                    },
                    {
                        "name": "Customer Segmentation",
                        "description": "Identifying valuable customer segments",
                        "demo_script": "User: 'How can we target our marketing better?'\nAI: 'I can segment your customers based on purchase history, browsing behavior, and demographics to identify your most valuable segments and personalize marketing efforts.'",
                        "business_value": "Enables targeted marketing and personalized customer experiences."
                    }
                ],
                "healthcare": [
                    {
                        "name": "Patient Scheduling Optimization",
                        "description": "Optimizing appointment scheduling",
                        "demo_script": "User: 'Our scheduling process is inefficient.'\nAI: 'I can optimize your appointment scheduling by analyzing historical no-show rates, procedure durations, and provider availability to maximize utilization and minimize wait times.'",
                        "business_value": "Improves provider utilization and patient satisfaction."
                    },
                    {
                        "name": "Compliance Monitoring",
                        "description": "Ensuring regulatory compliance",
                        "demo_script": "User: 'We struggle to keep up with healthcare regulations.'\nAI: 'I can monitor regulatory changes, audit your documentation for compliance issues, and provide alerts when potential compliance risks are detected.'",
                        "business_value": "Reduces compliance risks and associated penalties."
                    }
                ],
                "finance": [
                    {
                        "name": "Risk Assessment",
                        "description": "Evaluating financial risks",
                        "demo_script": "User: 'How can we better assess loan applicants?'\nAI: 'I can analyze applicant data, credit history, and market conditions to provide risk scores and recommendations for loan approval decisions.'",
                        "business_value": "Improves decision-making and reduces default rates."
                    },
                    {
                        "name": "Fraud Detection",
                        "description": "Identifying suspicious transactions",
                        "demo_script": "User: 'We need to reduce fraud losses.'\nAI: 'I can monitor transactions in real-time, flagging suspicious patterns and anomalies that may indicate fraudulent activity for immediate review.'",
                        "business_value": "Reduces fraud losses while minimizing false positives."
                    }
                ],
                "manufacturing": [
                    {
                        "name": "Predictive Maintenance",
                        "description": "Predicting equipment failures",
                        "demo_script": "User: 'Unexpected equipment downtime is costly for us.'\nAI: 'I can analyze equipment sensor data to predict potential failures before they occur, allowing for scheduled maintenance during planned downtime.'",
                        "business_value": "Reduces unplanned downtime and maintenance costs."
                    },
                    {
                        "name": "Quality Control",
                        "description": "Identifying quality issues",
                        "demo_script": "User: 'We need to improve product quality.'\nAI: 'I can analyze production data to identify factors contributing to quality issues and recommend process adjustments to improve product consistency.'",
                        "business_value": "Reduces defects and improves customer satisfaction."
                    }
                ],
                "technology": [
                    {
                        "name": "Code Analysis",
                        "description": "Analyzing and improving code",
                        "demo_script": "User: 'Our development process is slow.'\nAI: 'I can analyze your codebase to identify inefficiencies, potential bugs, and opportunities for optimization, helping your team develop more efficiently.'",
                        "business_value": "Improves code quality and developer productivity."
                    },
                    {
                        "name": "User Experience Analysis",
                        "description": "Evaluating and improving UX",
                        "demo_script": "User: 'Users find our software difficult to use.'\nAI: 'I can analyze user interaction data to identify pain points in your interface and recommend UX improvements based on best practices and user behavior.'",
                        "business_value": "Enhances user satisfaction and adoption rates."
                    }
                ]
            },
            "business_size_capabilities": {
                "small": [
                    {
                        "name": "Cost-Effective Automation",
                        "description": "Affordable automation solutions",
                        "demo_script": "User: 'We have limited resources for automation.'\nAI: 'I can help you identify high-impact, low-cost automation opportunities that provide the best ROI for your small business, starting with customer response automation.'",
                        "business_value": "Provides enterprise-level capabilities at small business prices."
                    },
                    {
                        "name": "Multi-Role Support",
                        "description": "Supporting multiple business functions",
                        "demo_script": "User: 'In our small team, we all wear multiple hats.'\nAI: 'I can assist with various functions from marketing to customer service to accounting, providing versatile support for your multi-role team members.'",
                        "business_value": "Offers versatile support across multiple business functions."
                    }
                ],
                "medium": [
                    {
                        "name": "Scalable Workflows",
                        "description": "Workflows that scale with growth",
                        "demo_script": "User: 'We're growing rapidly and our processes can't keep up.'\nAI: 'I can help design and implement scalable workflows that accommodate your current needs while easily expanding as your business grows.'",
                        "business_value": "Supports business growth without process redesign."
                    },
                    {
                        "name": "Department Coordination",
                        "description": "Improving cross-department collaboration",
                        "demo_script": "User: 'Our departments don't communicate effectively.'\nAI: 'I can serve as a central information hub, ensuring consistent data sharing across departments and facilitating collaborative workflows.'",
                        "business_value": "Enhances cross-functional collaboration and efficiency."
                    }
                ],
                "enterprise": [
                    {
                        "name": "Enterprise Integration",
                        "description": "Integrating with complex enterprise systems",
                        "demo_script": "User: 'We have a complex ecosystem of enterprise systems.'\nAI: 'I can integrate with your ERP, CRM, HCM, and other enterprise systems to provide a unified interface and consistent data across your organization.'",
                        "business_value": "Provides unified access to disparate enterprise systems."
                    },
                    {
                        "name": "Global Coordination",
                        "description": "Supporting global operations",
                        "demo_script": "User: 'We operate in multiple countries with different regulations.'\nAI: 'I can help coordinate global operations by managing region-specific requirements, supporting multiple languages, and ensuring consistent processes worldwide.'",
                        "business_value": "Enables consistent global operations with local adaptations."
                    }
                ]
            }
        }
        
        # Save the default capabilities data
        with open(self.capabilities_data_path, 'w') as f:
            json.dump(default_capabilities, f, indent=4)
            
        return default_capabilities
    
    def get_relevant_capabilities(self, 
                                 industry: str, 
                                 business_size: str,
                                 specific_interests: Optional[List[str]] = None) -> Dict:
        """
        Get capabilities relevant to the business context.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business (small, medium, enterprise)
            specific_interests: Optional list of specific capability interests
            
        Returns:
            Dict: Relevant capabilities for the business context
        """
        # Normalize inputs to lowercase
        industry = industry.lower()
        business_size = business_size.lower()
        
        # Always include core capabilities
        relevant_capabilities = {
            "core_capabilities": list(self.capabilities_data["core_capabilities"].values())
        }
        
        # Add industry-specific capabilities if available
        if industry in self.capabilities_data["industry_specific_capabilities"]:
            relevant_capabilities["industry_capabilities"] = self.capabilities_data["industry_specific_capabilities"][industry]
        else:
            # Default to technology if industry not found
            relevant_capabilities["industry_capabilities"] = self.capabilities_data["industry_specific_capabilities"]["technology"]
        
        # Add business size capabilities if available
        if business_size in self.capabilities_data["business_size_capabilities"]:
            relevant_capabilities["size_capabilities"] = self.capabilities_data["business_size_capabilities"][business_size]
        else:
            # Default to medium if size not found
            relevant_capabilities["size_capabilities"] = self.capabilities_data["business_size_capabilities"]["medium"]
        
        # Filter by specific interests if provided
        if specific_interests:
            filtered_capabilities = {"core_capabilities": [], "industry_capabilities": [], "size_capabilities": []}
            
            # Normalize interests to lowercase for case-insensitive matching
            interests_lower = [interest.lower() for interest in specific_interests]
            
            # Filter core capabilities
            for capability in relevant_capabilities["core_capabilities"]:
                if any(interest in capability["name"].lower() or interest in capability["description"].lower() for interest in interests_lower):
                    filtered_capabilities["core_capabilities"].append(capability)
            
            # Filter industry capabilities
            for capability in relevant_capabilities["industry_capabilities"]:
                if any(interest in capability["name"].lower() or interest in capability["description"].lower() for interest in interests_lower):
                    filtered_capabilities["industry_capabilities"].append(capability)
            
            # Filter size capabilities
            for capability in relevant_capabilities["size_capabilities"]:
                if any(interest in capability["name"].lower() or interest in capability["description"].lower() for interest in interests_lower):
                    filtered_capabilities["size_capabilities"].append(capability)
            
            # If we found any matching capabilities, use the filtered set
            if (filtered_capabilities["core_capabilities"] or 
                filtered_capabilities["industry_capabilities"] or 
                filtered_capabilities["size_capabilities"]):
                relevant_capabilities = filtered_capabilities
        
        return relevant_capabilities
    
    def generate_capability_demonstration(self, 
                                         industry: str, 
                                         business_size: str,
                                         specific_interests: Optional[List[str]] = None,
                                         max_capabilities: int = 5) -> str:
        """
        Generate a demonstration of relevant capabilities.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business
            specific_interests: Optional list of specific capability interests
            max_capabilities: Maximum number of capabilities to demonstrate
            
        Returns:
            str: A formatted capability demonstration
        """
        relevant_capabilities = self.get_relevant_capabilities(industry, business_size, specific_interests)
        
        # Combine all capabilities into a single list
        all_capabilities = (
            relevant_capabilities.get("core_capabilities", []) +
            relevant_capabilities.get("industry_capabilities", []) +
            relevant_capabilities.get("size_capabilities", [])
        )
        
        # Shuffle and limit to max_capabilities
        random.shuffle(all_capabilities)
        selected_capabilities = all_capabilities[:max_capabilities]
        
        # Generate demonstration
        demonstration = f"Capability Demonstration for {industry.capitalize()} ({business_size.capitalize()} Business)\n"
        demonstration += f"{'=' * len(demonstration)}\n\n"
        
        for i, capability in enumerate(selected_capabilities, 1):
            demonstration += f"{i}. {capability['name']}\n"
            demonstration += f"   {capability['description']}\n\n"
            demonstration += f"   Demo:\n"
            demonstration += f"   {capability['demo_script']}\n\n"
            demonstration += f"   Business Value:\n"
            demonstration += f"   {capability['business_value']}\n\n"
        
        return demonstration
    
    def update_capabilities_data(self, new_data: Dict) -> None:
        """
        Update the capabilities data with new information.
        
        Args:
            new_data: New capabilities data to add
        """
        # Merge new data with existing capabilities data
        for category, category_data in new_data.items():
            if category in self.capabilities_data:
                if isinstance(category_data, dict):
                    for key, value in category_data.items():
                        if key in self.capabilities_data[category]:
                            # Update existing entry
                            if isinstance(value, dict) and isinstance(self.capabilities_data[category][key], dict):
                                self.capabilities_data[category][key].update(value)
                            else:
                                self.capabilities_data[category][key] = value
                        else:
                            # Add new entry
                            self.capabilities_data[category][key] = value
                elif isinstance(category_data, list):
                    # For list types, append new items
                    self.capabilities_data[category].extend(category_data)
            else:
                # Add new category
                self.capabilities_data[category] = category_data
                
        # Save updated capabilities data
        with open(self.capabilities_data_path, 'w') as f:
            json.dump(self.capabilities_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    showcase = CapabilityShowcase()
    
    # Generate a capability demonstration for a retail business
    demonstration = showcase.generate_capability_demonstration(
        industry="retail",
        business_size="medium",
        specific_interests=["inventory", "customer"]
    )
    
    print(demonstration)
