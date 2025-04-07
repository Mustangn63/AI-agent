"""
Value Proposition Generator Module

This module generates tailored value propositions for the AI agent based on 
business type, size, industry, and user role.
"""

import json
import random
from typing import Dict, List, Optional

class ValuePropositionGenerator:
    """
    Generates tailored value propositions for the AI agent based on business context.
    """
    
    def __init__(self, knowledge_base_path: str = "knowledge_base.json"):
        """
        Initialize the Value Proposition Generator.
        
        Args:
            knowledge_base_path: Path to the knowledge base file containing industry-specific data
        """
        self.knowledge_base_path = knowledge_base_path
        self.knowledge_base = self._load_knowledge_base()
        
    def _load_knowledge_base(self) -> Dict:
        """
        Load the knowledge base from file.
        
        Returns:
            Dict: The knowledge base data
        """
        try:
            with open(self.knowledge_base_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default knowledge base if file not found or invalid
            return self._create_default_knowledge_base()
    
    def _create_default_knowledge_base(self) -> Dict:
        """
        Create a default knowledge base with basic industry and role information.
        
        Returns:
            Dict: Default knowledge base
        """
        default_kb = {
            "industries": {
                "retail": {
                    "pain_points": ["inventory management", "customer engagement", "sales forecasting"],
                    "benefits": ["increased sales", "improved customer retention", "optimized inventory"],
                    "metrics": ["sales growth", "customer satisfaction", "inventory turnover"]
                },
                "healthcare": {
                    "pain_points": ["patient scheduling", "record management", "regulatory compliance"],
                    "benefits": ["improved patient care", "reduced administrative burden", "compliance assurance"],
                    "metrics": ["patient satisfaction", "administrative time saved", "compliance rate"]
                },
                "finance": {
                    "pain_points": ["risk assessment", "fraud detection", "customer service"],
                    "benefits": ["reduced risk", "fraud prevention", "enhanced customer experience"],
                    "metrics": ["risk reduction percentage", "fraud detection rate", "customer satisfaction"]
                },
                "manufacturing": {
                    "pain_points": ["production efficiency", "quality control", "supply chain management"],
                    "benefits": ["increased productivity", "improved quality", "optimized supply chain"],
                    "metrics": ["production rate", "defect reduction", "supply chain cost reduction"]
                },
                "technology": {
                    "pain_points": ["development speed", "customer support", "product innovation"],
                    "benefits": ["faster development", "improved support", "enhanced innovation"],
                    "metrics": ["development time reduction", "support resolution time", "innovation rate"]
                }
            },
            "business_sizes": {
                "small": {
                    "pain_points": ["limited resources", "cost management", "growth challenges"],
                    "benefits": ["cost efficiency", "resource optimization", "scalable growth"],
                    "metrics": ["cost reduction", "resource utilization", "growth rate"]
                },
                "medium": {
                    "pain_points": ["scaling operations", "process standardization", "talent management"],
                    "benefits": ["operational efficiency", "standardized processes", "improved talent utilization"],
                    "metrics": ["operational cost reduction", "process efficiency", "employee productivity"]
                },
                "enterprise": {
                    "pain_points": ["organizational complexity", "global coordination", "innovation at scale"],
                    "benefits": ["simplified complexity", "enhanced coordination", "scalable innovation"],
                    "metrics": ["organizational efficiency", "coordination effectiveness", "innovation impact"]
                }
            },
            "roles": {
                "executive": {
                    "pain_points": ["strategic decision-making", "performance visibility", "resource allocation"],
                    "benefits": ["data-driven decisions", "real-time performance insights", "optimized resource allocation"],
                    "metrics": ["decision quality", "performance improvement", "resource efficiency"]
                },
                "manager": {
                    "pain_points": ["team productivity", "project tracking", "resource management"],
                    "benefits": ["enhanced team output", "real-time project visibility", "efficient resource use"],
                    "metrics": ["team productivity", "project completion rate", "resource utilization"]
                },
                "specialist": {
                    "pain_points": ["task efficiency", "knowledge access", "collaboration"],
                    "benefits": ["automated workflows", "instant knowledge access", "seamless collaboration"],
                    "metrics": ["task completion time", "knowledge utilization", "collaboration effectiveness"]
                }
            },
            "value_proposition_templates": [
                "Our AI agent helps {industry} businesses address {pain_point} by providing {benefit}, resulting in {metric_improvement}.",
                "For {business_size} businesses in {industry}, our AI agent transforms {pain_point} into {benefit}, with measurable improvements in {metric}.",
                "{role}s in {industry} use our AI agent to overcome {pain_point}, achieving {benefit} and improving {metric}.",
                "Our AI agent is specifically designed to help {business_size} {industry} businesses turn {pain_point} challenges into {benefit} opportunities.",
                "By addressing {pain_point} for {role}s in {industry}, our AI agent delivers {benefit} with proven impact on {metric}."
            ]
        }
        
        # Save the default knowledge base
        with open(self.knowledge_base_path, 'w') as f:
            json.dump(default_kb, f, indent=4)
            
        return default_kb
    
    def generate_value_proposition(self, 
                                  industry: str, 
                                  business_size: str, 
                                  role: str,
                                  custom_context: Optional[Dict] = None) -> str:
        """
        Generate a tailored value proposition based on business context.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business (small, medium, enterprise)
            role: The role of the user (executive, manager, specialist)
            custom_context: Additional custom context for more personalized propositions
            
        Returns:
            str: A tailored value proposition
        """
        # Normalize inputs to lowercase
        industry = industry.lower()
        business_size = business_size.lower()
        role = role.lower()
        
        # Get industry data or default to technology if not found
        industry_data = self.knowledge_base["industries"].get(
            industry, self.knowledge_base["industries"]["technology"]
        )
        
        # Get business size data or default to medium if not found
        size_data = self.knowledge_base["business_sizes"].get(
            business_size, self.knowledge_base["business_sizes"]["medium"]
        )
        
        # Get role data or default to manager if not found
        role_data = self.knowledge_base["roles"].get(
            role, self.knowledge_base["roles"]["manager"]
        )
        
        # Select random elements for the value proposition
        pain_point = random.choice(industry_data["pain_points"] + size_data["pain_points"])
        benefit = random.choice(industry_data["benefits"] + size_data["benefits"])
        metric = random.choice(industry_data["metrics"] + size_data["metrics"])
        
        # Select a random template
        template = random.choice(self.knowledge_base["value_proposition_templates"])
        
        # Format the template with the selected elements
        value_proposition = template.format(
            industry=industry,
            business_size=business_size,
            role=role,
            pain_point=pain_point,
            benefit=benefit,
            metric=metric,
            metric_improvement=f"improved {metric}"
        )
        
        return value_proposition
    
    def generate_multiple_propositions(self,
                                      industry: str,
                                      business_size: str,
                                      role: str,
                                      count: int = 3) -> List[str]:
        """
        Generate multiple value propositions for the same business context.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business
            role: The role of the user
            count: Number of propositions to generate
            
        Returns:
            List[str]: A list of value propositions
        """
        propositions = []
        for _ in range(count):
            proposition = self.generate_value_proposition(industry, business_size, role)
            propositions.append(proposition)
            
        return propositions
    
    def update_knowledge_base(self, new_data: Dict) -> None:
        """
        Update the knowledge base with new data.
        
        Args:
            new_data: New data to add to the knowledge base
        """
        # Merge new data with existing knowledge base
        for category, category_data in new_data.items():
            if category in self.knowledge_base:
                for key, value in category_data.items():
                    if key in self.knowledge_base[category]:
                        # Update existing entry
                        self.knowledge_base[category][key].update(value)
                    else:
                        # Add new entry
                        self.knowledge_base[category][key] = value
            else:
                # Add new category
                self.knowledge_base[category] = category_data
                
        # Save updated knowledge base
        with open(self.knowledge_base_path, 'w') as f:
            json.dump(self.knowledge_base, f, indent=4)


# Example usage
if __name__ == "__main__":
    generator = ValuePropositionGenerator()
    
    # Generate a single value proposition
    proposition = generator.generate_value_proposition(
        industry="retail",
        business_size="small",
        role="manager"
    )
    print("Single Value Proposition:")
    print(proposition)
    print()
    
    # Generate multiple value propositions
    propositions = generator.generate_multiple_propositions(
        industry="healthcare",
        business_size="enterprise",
        role="executive",
        count=3
    )
    print("Multiple Value Propositions:")
    for i, prop in enumerate(propositions, 1):
        print(f"{i}. {prop}")
