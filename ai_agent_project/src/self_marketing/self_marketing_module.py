"""
Self-Marketing Module Integration

This module integrates all self-marketing components into a cohesive system.
"""

from typing import Dict, List, Optional

from .value_proposition_generator import ValuePropositionGenerator
from .roi_calculator import ROICalculator
from .capability_showcase import CapabilityShowcase
from .competitive_differentiator import CompetitiveDifferentiator
from .trust_builder import TrustBuilder

class SelfMarketingModule:
    """
    Integrates all self-marketing components to provide comprehensive self-marketing capabilities.
    """
    
    def __init__(self):
        """
        Initialize the Self-Marketing Module with all component modules.
        """
        self.value_proposition_generator = ValuePropositionGenerator()
        self.roi_calculator = ROICalculator()
        self.capability_showcase = CapabilityShowcase()
        self.competitive_differentiator = CompetitiveDifferentiator()
        self.trust_builder = TrustBuilder()
    
    def generate_marketing_package(self,
                                  industry: str,
                                  business_size: str,
                                  role: str,
                                  annual_revenue: float = 1000000,
                                  employees_count: int = 50,
                                  specific_interests: Optional[List[str]] = None) -> Dict:
        """
        Generate a comprehensive marketing package tailored to the business context.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business (small, medium, enterprise)
            role: The role of the user (executive, manager, specialist)
            annual_revenue: Annual revenue of the business
            employees_count: Number of employees in the business
            specific_interests: Optional list of specific capability interests
            
        Returns:
            Dict: A comprehensive marketing package with all components
        """
        # Generate value propositions
        value_propositions = self.value_proposition_generator.generate_multiple_propositions(
            industry=industry,
            business_size=business_size,
            role=role,
            count=3
        )
        
        # Calculate ROI
        roi_data = self.roi_calculator.calculate_roi(
            industry=industry,
            business_size=business_size,
            annual_revenue=annual_revenue,
            employees_count=employees_count
        )
        roi_summary = self.roi_calculator.generate_roi_summary(roi_data)
        
        # Generate capability demonstration
        capability_demo = self.capability_showcase.generate_capability_demonstration(
            industry=industry,
            business_size=business_size,
            specific_interests=specific_interests,
            max_capabilities=5
        )
        
        # Generate competitive comparison
        competitive_comparison = self.competitive_differentiator.generate_competitive_comparison(
            industry=industry,
            business_size=business_size,
            comparison_type="all"
        )
        
        # Generate trust statement
        trust_statement = self.trust_builder.generate_trust_statement(
            industry=industry,
            focus_areas=["security", "privacy", "ethics"]
        )
        
        # Compile marketing package
        marketing_package = {
            "business_context": {
                "industry": industry,
                "business_size": business_size,
                "role": role
            },
            "value_propositions": value_propositions,
            "roi_analysis": {
                "summary": roi_summary,
                "detailed_data": roi_data
            },
            "capability_demonstration": capability_demo,
            "competitive_comparison": competitive_comparison,
            "trust_statement": trust_statement
        }
        
        return marketing_package
    
    def generate_elevator_pitch(self,
                               industry: str,
                               business_size: str,
                               role: str) -> str:
        """
        Generate a concise elevator pitch tailored to the business context.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business
            role: The role of the user
            
        Returns:
            str: A concise elevator pitch
        """
        # Get a single value proposition
        value_proposition = self.value_proposition_generator.generate_value_proposition(
            industry=industry,
            business_size=business_size,
            role=role
        )
        
        # Get relevant capabilities
        relevant_capabilities = self.capability_showcase.get_relevant_capabilities(
            industry=industry,
            business_size=business_size
        )
        
        # Select one core capability and one industry-specific capability
        core_capability = relevant_capabilities["core_capabilities"][0] if relevant_capabilities["core_capabilities"] else None
        industry_capability = relevant_capabilities["industry_capabilities"][0] if relevant_capabilities["industry_capabilities"] else None
        
        # Generate elevator pitch
        pitch = f"Our AI agent is designed specifically for {business_size} businesses in the {industry} industry. "
        pitch += value_proposition + " "
        
        if core_capability:
            pitch += f"With {core_capability['name']}, {core_capability['description'].lower()}. "
        
        if industry_capability:
            pitch += f"For {industry} specifically, we offer {industry_capability['name']}, {industry_capability['description'].lower()}. "
        
        pitch += "We'd be happy to provide a detailed demonstration of how our AI agent can benefit your specific business needs."
        
        return pitch
    
    def generate_detailed_proposal(self,
                                  industry: str,
                                  business_size: str,
                                  role: str,
                                  company_name: str,
                                  annual_revenue: float = 1000000,
                                  employees_count: int = 50,
                                  specific_interests: Optional[List[str]] = None) -> str:
        """
        Generate a detailed business proposal tailored to the specific company.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business
            role: The role of the user
            company_name: The name of the company
            annual_revenue: Annual revenue of the business
            employees_count: Number of employees in the business
            specific_interests: Optional list of specific capability interests
            
        Returns:
            str: A detailed business proposal
        """
        # Generate marketing package
        marketing_package = self.generate_marketing_package(
            industry=industry,
            business_size=business_size,
            role=role,
            annual_revenue=annual_revenue,
            employees_count=employees_count,
            specific_interests=specific_interests
        )
        
        # Extract components
        value_propositions = marketing_package["value_propositions"]
        roi_summary = marketing_package["roi_analysis"]["summary"]
        capability_demo = marketing_package["capability_demonstration"]
        competitive_comparison = marketing_package["competitive_comparison"]
        trust_statement = marketing_package["trust_statement"]
        
        # Generate proposal
        proposal = f"# AI Agent Implementation Proposal for {company_name}\n\n"
        
        proposal += "## Executive Summary\n\n"
        proposal += f"This proposal outlines how our AI agent can benefit {company_name} by addressing key challenges in the {industry} industry. "
        proposal += f"As a {business_size} business, {company_name} can leverage our AI agent to improve efficiency, reduce costs, and enhance customer experiences. "
        proposal += f"The following sections detail the specific value propositions, return on investment, capabilities, competitive advantages, and trust considerations relevant to {company_name}.\n\n"
        
        proposal += "## Value Propositions\n\n"
        for i, prop in enumerate(value_propositions, 1):
            proposal += f"{i}. {prop}\n\n"
        
        proposal += "## Return on Investment Analysis\n\n"
        proposal += roi_summary + "\n\n"
        
        proposal += "## Capabilities Demonstration\n\n"
        proposal += capability_demo + "\n\n"
        
        proposal += "## Competitive Advantages\n\n"
        proposal += competitive_comparison + "\n\n"
        
        proposal += "## Trust and Security Considerations\n\n"
        proposal += trust_statement + "\n\n"
        
        proposal += "## Implementation Timeline\n\n"
        proposal += "1. **Discovery Phase (Week 1-2)**: Detailed assessment of your specific requirements and integration points.\n"
        proposal += "2. **Configuration Phase (Week 3-4)**: Customization of the AI agent to your specific business context.\n"
        proposal += "3. **Integration Phase (Week 5-6)**: Integration with your existing systems and data sources.\n"
        proposal += "4. **Testing Phase (Week 7-8)**: Comprehensive testing and validation of the AI agent.\n"
        proposal += "5. **Deployment Phase (Week 9)**: Deployment of the AI agent to production.\n"
        proposal += "6. **Training Phase (Week 10)**: Training of your team on using and managing the AI agent.\n"
        proposal += "7. **Optimization Phase (Ongoing)**: Continuous improvement and optimization of the AI agent based on feedback and performance data.\n\n"
        
        proposal += "## Next Steps\n\n"
        proposal += "1. Schedule a detailed discovery meeting to discuss your specific requirements.\n"
        proposal += "2. Conduct a proof of concept demonstration with your actual data.\n"
        proposal += "3. Finalize implementation details and timeline.\n"
        proposal += "4. Begin the implementation process.\n\n"
        
        proposal += "We look forward to partnering with you to implement our AI agent and help drive success for your business."
        
        return proposal


# Example usage
if __name__ == "__main__":
    self_marketing = SelfMarketingModule()
    
    # Generate an elevator pitch
    pitch = self_marketing.generate_elevator_pitch(
        industry="retail",
        business_size="medium",
        role="executive"
    )
    
    print("Elevator Pitch:")
    print(pitch)
    print("\n" + "="*50 + "\n")
    
    # Generate a detailed proposal
    proposal = self_marketing.generate_detailed_proposal(
        industry="retail",
        business_size="medium",
        role="executive",
        company_name="Acme Retail Inc.",
        annual_revenue=5000000,
        employees_count=100,
        specific_interests=["inventory", "customer"]
    )
    
    print("Detailed Proposal Preview:")
    print(proposal[:500] + "...")
