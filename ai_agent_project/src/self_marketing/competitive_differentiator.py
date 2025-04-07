"""
Competitive Differentiator Module

This module highlights advantages of the AI agent over alternative solutions
or human-performed tasks.
"""

import json
import random
from typing import Dict, List, Optional

class CompetitiveDifferentiator:
    """
    Highlights advantages of the AI agent over alternatives based on business context.
    """
    
    def __init__(self, differentiators_data_path: str = "differentiators.json"):
        """
        Initialize the Competitive Differentiator.
        
        Args:
            differentiators_data_path: Path to the differentiators data file
        """
        self.differentiators_data_path = differentiators_data_path
        self.differentiators_data = self._load_differentiators_data()
        
    def _load_differentiators_data(self) -> Dict:
        """
        Load the differentiators data from file.
        
        Returns:
            Dict: The differentiators data
        """
        try:
            with open(self.differentiators_data_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default differentiators data if file not found or invalid
            return self._create_default_differentiators_data()
    
    def _create_default_differentiators_data(self) -> Dict:
        """
        Create default differentiators data with comparisons to alternatives.
        
        Returns:
            Dict: Default differentiators data
        """
        default_differentiators = {
            "vs_human_workers": {
                "speed": {
                    "title": "Processing Speed",
                    "description": "Our AI agent processes information and performs tasks significantly faster than human workers.",
                    "comparison": "While a human might take hours to analyze customer feedback data, our AI can process thousands of entries in minutes.",
                    "business_impact": "Reduced processing time means faster insights and quicker response to market changes."
                },
                "consistency": {
                    "title": "Consistency",
                    "description": "Our AI agent performs with consistent quality regardless of time of day or workload.",
                    "comparison": "Human performance naturally varies due to fatigue, distractions, or workload, while our AI maintains the same high quality standards 24/7.",
                    "business_impact": "Consistent quality leads to reliable operations and predictable outcomes."
                },
                "scalability": {
                    "title": "Scalability",
                    "description": "Our AI agent can scale operations instantly without additional hiring or training.",
                    "comparison": "Scaling human operations requires hiring, onboarding, and training, which can take weeks or months.",
                    "business_impact": "Rapidly adapt to changing business demands without staffing constraints."
                },
                "cost_efficiency": {
                    "title": "Cost Efficiency",
                    "description": "Our AI agent provides significant cost savings compared to equivalent human resources.",
                    "comparison": "The annual cost of our AI solution is typically less than the salary of a single employee, yet can perform the work of multiple staff members.",
                    "business_impact": "Reduced operational costs while maintaining or improving output quality and quantity."
                },
                "availability": {
                    "title": "24/7 Availability",
                    "description": "Our AI agent is available around the clock without breaks, vacations, or sick days.",
                    "comparison": "Human workers typically work 8 hours per day, 5 days per week, with additional time off for holidays, vacations, and sick leave.",
                    "business_impact": "Continuous operations and support without interruptions or staffing concerns."
                }
            },
            "vs_other_ai_solutions": {
                "adaptability": {
                    "title": "Business Adaptability",
                    "description": "Our AI agent adapts to your specific business context, industry, and organizational structure.",
                    "comparison": "Many AI solutions offer one-size-fits-all approaches that don't account for your unique business environment.",
                    "business_impact": "A solution that understands and adapts to your business rather than forcing you to adapt to it."
                },
                "self_improvement": {
                    "title": "Continuous Learning",
                    "description": "Our AI agent continuously learns from interactions and improves its performance over time.",
                    "comparison": "Many AI solutions remain static after deployment, requiring manual updates to improve functionality.",
                    "business_impact": "An increasingly valuable asset that grows more effective with use rather than depreciating."
                },
                "integration": {
                    "title": "Seamless Integration",
                    "description": "Our AI agent integrates easily with your existing systems and workflows.",
                    "comparison": "Many AI solutions require significant changes to your current systems or operate as isolated tools.",
                    "business_impact": "Maximize the value of your existing technology investments while adding new capabilities."
                },
                "transparency": {
                    "title": "Explainable AI",
                    "description": "Our AI agent provides clear explanations for its recommendations and actions.",
                    "comparison": "Many AI solutions operate as black boxes, making decisions without explaining their reasoning.",
                    "business_impact": "Build trust with stakeholders and ensure accountability in AI-assisted decisions."
                },
                "customization": {
                    "title": "Deep Customization",
                    "description": "Our AI agent can be extensively customized to meet your specific requirements.",
                    "comparison": "Many AI solutions offer limited customization options, constraining their usefulness for unique business needs.",
                    "business_impact": "A solution that fits your business perfectly rather than forcing compromises."
                }
            },
            "industry_specific_differentiators": {
                "retail": [
                    {
                        "title": "Customer Behavior Understanding",
                        "description": "Our AI agent has specialized capabilities for analyzing retail customer behavior patterns.",
                        "comparison": "Generic solutions lack retail-specific insights and may miss important patterns in customer data.",
                        "business_impact": "More accurate customer segmentation and personalized marketing opportunities."
                    },
                    {
                        "title": "Inventory Optimization",
                        "description": "Our AI agent includes advanced inventory management algorithms designed specifically for retail operations.",
                        "comparison": "General-purpose AI solutions typically lack the specialized algorithms needed for effective retail inventory management.",
                        "business_impact": "Reduced carrying costs and stockouts while improving product availability."
                    }
                ],
                "healthcare": [
                    {
                        "title": "HIPAA Compliance",
                        "description": "Our AI agent is designed with healthcare compliance requirements built in.",
                        "comparison": "Many AI solutions require extensive modification to meet healthcare regulatory requirements.",
                        "business_impact": "Reduced compliance risk and implementation time for healthcare organizations."
                    },
                    {
                        "title": "Clinical Workflow Integration",
                        "description": "Our AI agent understands clinical workflows and integrates seamlessly with healthcare processes.",
                        "comparison": "Generic AI solutions often disrupt clinical workflows, creating adoption barriers.",
                        "business_impact": "Higher adoption rates and less disruption to critical healthcare operations."
                    }
                ],
                "finance": [
                    {
                        "title": "Regulatory Compliance",
                        "description": "Our AI agent includes financial regulatory compliance features built in.",
                        "comparison": "Many AI solutions require extensive customization to meet financial regulatory requirements.",
                        "business_impact": "Reduced compliance risk and implementation time for financial institutions."
                    },
                    {
                        "title": "Fraud Detection Specialization",
                        "description": "Our AI agent includes advanced fraud detection algorithms designed specifically for financial transactions.",
                        "comparison": "General-purpose AI solutions typically lack the specialized pattern recognition needed for effective fraud detection.",
                        "business_impact": "Reduced fraud losses while minimizing false positives that impact legitimate customers."
                    }
                ],
                "manufacturing": [
                    {
                        "title": "Production Optimization",
                        "description": "Our AI agent includes specialized algorithms for manufacturing process optimization.",
                        "comparison": "Generic AI solutions lack the specific capabilities needed to optimize complex manufacturing processes.",
                        "business_impact": "Improved production efficiency and reduced waste in manufacturing operations."
                    },
                    {
                        "title": "Supply Chain Integration",
                        "description": "Our AI agent has built-in capabilities for manufacturing supply chain management.",
                        "comparison": "Many AI solutions treat supply chain as a separate function rather than an integrated part of manufacturing.",
                        "business_impact": "More resilient and efficient supply chain operations integrated with production."
                    }
                ],
                "technology": [
                    {
                        "title": "Developer Workflow Integration",
                        "description": "Our AI agent integrates seamlessly with software development tools and processes.",
                        "comparison": "Many AI solutions operate outside the development workflow, creating friction for technology teams.",
                        "business_impact": "Higher adoption rates and productivity improvements for development teams."
                    },
                    {
                        "title": "Technical Debt Reduction",
                        "description": "Our AI agent helps identify and address technical debt in software systems.",
                        "comparison": "Generic AI solutions typically focus on new development rather than improving existing systems.",
                        "business_impact": "More sustainable technology operations with reduced maintenance costs over time."
                    }
                ]
            },
            "business_size_differentiators": {
                "small": [
                    {
                        "title": "Cost-Effective Implementation",
                        "description": "Our AI agent offers implementation options specifically designed for small business budgets.",
                        "comparison": "Many AI solutions have high implementation costs that make them impractical for small businesses.",
                        "business_impact": "Access to enterprise-level AI capabilities within small business budget constraints."
                    },
                    {
                        "title": "Minimal IT Requirements",
                        "description": "Our AI agent requires minimal IT infrastructure and support.",
                        "comparison": "Many AI solutions require significant IT resources that small businesses typically don't have.",
                        "business_impact": "Easy implementation and maintenance without dedicated IT staff."
                    }
                ],
                "medium": [
                    {
                        "title": "Growth-Friendly Scaling",
                        "description": "Our AI agent scales easily as your business grows without requiring reimplementation.",
                        "comparison": "Many solutions that work for medium businesses require replacement as the business grows.",
                        "business_impact": "A long-term solution that grows with your business rather than constraining growth."
                    },
                    {
                        "title": "Departmental Coordination",
                        "description": "Our AI agent facilitates coordination between departments, addressing a common pain point for medium businesses.",
                        "comparison": "Many solutions focus on individual department efficiency without addressing cross-department coordination.",
                        "business_impact": "Improved operational efficiency across the entire organization, not just within departments."
                    }
                ],
                "enterprise": [
                    {
                        "title": "Enterprise-Grade Security",
                        "description": "Our AI agent includes enterprise-level security features and compliance capabilities.",
                        "comparison": "Many AI solutions lack the robust security features required for enterprise deployment.",
                        "business_impact": "Reduced security risk and easier compliance with corporate security policies."
                    },
                    {
                        "title": "Global Deployment Support",
                        "description": "Our AI agent supports global deployment with multi-region, multi-language capabilities.",
                        "comparison": "Many AI solutions are designed for single-region deployment with limited language support.",
                        "business_impact": "Consistent global operations with appropriate localization where needed."
                    }
                ]
            }
        }
        
        # Save the default differentiators data
        with open(self.differentiators_data_path, 'w') as f:
            json.dump(default_differentiators, f, indent=4)
            
        return default_differentiators
    
    def get_relevant_differentiators(self, 
                                    industry: str, 
                                    business_size: str,
                                    comparison_type: str = "all",
                                    max_differentiators: int = 5) -> Dict:
        """
        Get differentiators relevant to the business context.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business (small, medium, enterprise)
            comparison_type: Type of comparison to focus on ("human", "ai", or "all")
            max_differentiators: Maximum number of differentiators to return
            
        Returns:
            Dict: Relevant differentiators for the business context
        """
        # Normalize inputs to lowercase
        industry = industry.lower()
        business_size = business_size.lower()
        comparison_type = comparison_type.lower()
        
        relevant_differentiators = {}
        
        # Add human worker comparisons if requested
        if comparison_type in ["human", "all"]:
            # Select a subset of human worker differentiators
            human_keys = list(self.differentiators_data["vs_human_workers"].keys())
            random.shuffle(human_keys)
            selected_human_keys = human_keys[:min(3, len(human_keys))]
            
            relevant_differentiators["vs_human_workers"] = {
                key: self.differentiators_data["vs_human_workers"][key] 
                for key in selected_human_keys
            }
        
        # Add AI solution comparisons if requested
        if comparison_type in ["ai", "all"]:
            # Select a subset of AI solution differentiators
            ai_keys = list(self.differentiators_data["vs_other_ai_solutions"].keys())
            random.shuffle(ai_keys)
            selected_ai_keys = ai_keys[:min(3, len(ai_keys))]
            
            relevant_differentiators["vs_other_ai_solutions"] = {
                key: self.differentiators_data["vs_other_ai_solutions"][key] 
                for key in selected_ai_keys
            }
        
        # Add industry-specific differentiators if available
        if industry in self.differentiators_data["industry_specific_differentiators"]:
            industry_differentiators = self.differentiators_data["industry_specific_differentiators"][industry]
            # Select a subset if there are more than 2
            if len(industry_differentiators) > 2:
                random.shuffle(industry_differentiators)
                industry_differentiators = industry_differentiators[:2]
            
            relevant_differentiators["industry_specific"] = industry_differentiators
        else:
            # Default to technology if industry not found
            industry_differentiators = self.differentiators_data["industry_specific_differentiators"]["technology"]
            # Select a subset if there are more than 2
            if len(industry_differentiators) > 2:
                random.shuffle(industry_differentiators)
                industry_differentiators = industry_differentiators[:2]
            
            relevant_differentiators["industry_specific"] = industry_differentiators
        
        # Add business size differentiators if available
        if business_size in self.differentiators_data["business_size_differentiators"]:
            size_differentiators = self.differentiators_data["business_size_differentiators"][business_size]
            # Select a subset if there are more than 2
            if len(size_differentiators) > 2:
                random.shuffle(size_differentiators)
                size_differentiators = size_differentiators[:2]
            
            relevant_differentiators["business_size"] = size_differentiators
        else:
            # Default to medium if size not found
            size_differentiators = self.differentiators_data["business_size_differentiators"]["medium"]
            # Select a subset if there are more than 2
            if len(size_differentiators) > 2:
                random.shuffle(size_differentiators)
                size_differentiators = size_differentiators[:2]
            
            relevant_differentiators["business_size"] = size_differentiators
        
        return relevant_differentiators
    
    def generate_competitive_comparison(self, 
                                       industry: str, 
                                       business_size: str,
                                       comparison_type: str = "all") -> str:
        """
        Generate a competitive comparison based on business context.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business
            comparison_type: Type of comparison to focus on ("human", "ai", or "all")
            
        Returns:
            str: A formatted competitive comparison
        """
        relevant_differentiators = self.get_relevant_differentiators(
            industry, business_size, comparison_type
        )
        
        # Generate comparison
        comparison = f"Competitive Advantages for {industry.capitalize()} ({business_size.capitalize()} Business)\n"
        comparison += f"{'=' * len(comparison)}\n\n"
        
        # Add human worker comparisons if available
        if "vs_human_workers" in relevant_differentiators:
            comparison += f"## Advantages Over Human-Performed Tasks\n\n"
            
            for key, diff in relevant_differentiators["vs_human_workers"].items():
                comparison += f"### {diff['title']}\n"
                comparison += f"{diff['description']}\n\n"
                comparison += f"**Comparison:** {diff['comparison']}\n\n"
                comparison += f"**Business Impact:** {diff['business_impact']}\n\n"
        
        # Add AI solution comparisons if available
        if "vs_other_ai_solutions" in relevant_differentiators:
            comparison += f"## Advantages Over Other AI Solutions\n\n"
            
            for key, diff in relevant_differentiators["vs_other_ai_solutions"].items():
                comparison += f"### {diff['title']}\n"
                comparison += f"{diff['description']}\n\n"
                comparison += f"**Comparison:** {diff['comparison']}\n\n"
                comparison += f"**Business Impact:** {diff['business_impact']}\n\n"
        
        # Add industry-specific differentiators if available
        if "industry_specific" in relevant_differentiators:
            comparison += f"## {industry.capitalize()} Industry-Specific Advantages\n\n"
            
            for diff in relevant_differentiators["industry_specific"]:
                comparison += f"### {diff['title']}\n"
                comparison += f"{diff['description']}\n\n"
                comparison += f"**Comparison:** {diff['comparison']}\n\n"
                comparison += f"**Business Impact:** {diff['business_impact']}\n\n"
        
        # Add business size differentiators if available
        if "business_size" in relevant_differentiators:
            comparison += f"## {business_size.capitalize()} Business Size Advantages\n\n"
            
            for diff in relevant_differentiators["business_size"]:
                comparison += f"### {diff['title']}\n"
                comparison += f"{diff['description']}\n\n"
                comparison += f"**Comparison:** {diff['comparison']}\n\n"
                comparison += f"**Business Impact:** {diff['business_impact']}\n\n"
        
        return comparison
    
    def update_differentiators_data(self, new_data: Dict) -> None:
        """
        Update the differentiators data with new information.
        
        Args:
            new_data: New differentiators data to add
        """
        # Merge new data with existing differentiators data
        for category, category_data in new_data.items():
            if category in self.differentiators_data:
                if isinstance(category_data, dict):
                    for key, value in category_data.items():
                        if key in self.differentiators_data[category]:
                            # Update existing entry
                            if isinstance(value, dict) and isinstance(self.differentiators_data[category][key], dict):
                                self.differentiators_data[category][key].update(value)
                            else:
                                self.differentiators_data[category][key] = value
                        else:
                            # Add new entry
                            self.differentiators_data[category][key] = value
                elif isinstance(category_data, list):
                    # For list types, append new items
                    self.differentiators_data[category].extend(category_data)
            else:
                # Add new category
                self.differentiators_data[category] = category_data
                
        # Save updated differentiators data
        with open(self.differentiators_data_path, 'w') as f:
            json.dump(self.differentiators_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    differentiator = CompetitiveDifferentiator()
    
    # Generate a competitive comparison for a retail business
    comparison = differentiator.generate_competitive_comparison(
        industry="retail",
        business_size="medium",
        comparison_type="all"
    )
    
    print(comparison)
