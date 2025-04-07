"""
Business Context Adapter Module

This module integrates all business adaptability components into a cohesive system.
"""

from typing import Dict, List, Optional

from .industry_classifier import IndustryClassifier
from .business_size_analyzer import BusinessSizeAnalyzer
from .role_recognizer import RoleRecognizer

class BusinessContextAdapter:
    """
    Integrates all business adaptability components to provide comprehensive context adaptation.
    """
    
    def __init__(self):
        """
        Initialize the Business Context Adapter with all component modules.
        """
        self.industry_classifier = IndustryClassifier()
        self.business_size_analyzer = BusinessSizeAnalyzer()
        self.role_recognizer = RoleRecognizer()
    
    def analyze_business_context(self,
                               business_description: str,
                               job_title: str,
                               employees_count: Optional[int] = None,
                               annual_revenue: Optional[float] = None,
                               additional_info: Optional[Dict] = None) -> Dict:
        """
        Analyze the complete business context based on provided information.
        
        Args:
            business_description: Description of the business
            job_title: The user's job title
            employees_count: Optional number of employees
            annual_revenue: Optional annual revenue in USD
            additional_info: Optional dictionary with additional information
            
        Returns:
            Dict: Comprehensive business context analysis
        """
        # Extract additional information
        additional_keywords = additional_info.get("keywords", []) if additional_info else []
        role_additional_info = additional_info.get("role_info", "") if additional_info else ""
        industry_specific_metrics = additional_info.get("industry_metrics", {}) if additional_info else {}
        
        # Classify industry
        industry_classification = self.industry_classifier.classify_industry(
            business_description=business_description,
            additional_keywords=additional_keywords
        )
        
        # Get primary industry ID
        industry_id = industry_classification["primary_industry"]["id"]
        
        # Analyze business size
        size_analysis = self.business_size_analyzer.analyze_business_size(
            industry=industry_id,
            employees_count=employees_count,
            annual_revenue=annual_revenue,
            additional_metrics=industry_specific_metrics
        )
        
        # Recognize role
        role_recognition = self.role_recognizer.recognize_role(
            job_title=job_title,
            additional_info=role_additional_info,
            industry=industry_id
        )
        
        # Compile comprehensive context
        business_context = {
            "industry": {
                "id": industry_classification["primary_industry"]["id"],
                "name": industry_classification["primary_industry"]["name"],
                "confidence": industry_classification["primary_industry"]["confidence"],
                "sub_industry": industry_classification["sub_industry"] if industry_classification["sub_industry"]["id"] else None
            },
            "business_size": {
                "category": size_analysis["size_category"],
                "confidence": size_analysis["confidence"],
                "description": size_analysis["description"],
                "challenges": size_analysis["challenges"],
                "opportunities": size_analysis["opportunities"]
            },
            "user_role": {
                "organizational": {
                    "id": role_recognition["organizational_role"]["id"],
                    "name": role_recognition["organizational_role"]["name"],
                    "confidence": role_recognition["organizational_role"]["confidence"]
                },
                "functional": {
                    "id": role_recognition["functional_role"]["id"],
                    "name": role_recognition["functional_role"]["name"],
                    "confidence": role_recognition["functional_role"]["confidence"]
                },
                "industry_specific": role_recognition["industry_specific_role"] if role_recognition["industry_specific_role"] else None,
                "communication_strategy": role_recognition["communication_strategy"]
            },
            "detailed_analysis": {
                "industry_matches": industry_classification["all_matches"],
                "size_metrics": size_analysis["metrics_analysis"],
                "role_matches": role_recognition["all_matches"]
            }
        }
        
        return business_context
    
    def generate_adaptation_strategy(self, business_context: Dict) -> Dict:
        """
        Generate a comprehensive adaptation strategy based on business context.
        
        Args:
            business_context: The business context analysis
            
        Returns:
            Dict: Adaptation strategy for the business context
        """
        # Extract key context elements
        industry_id = business_context["industry"]["id"]
        industry_name = business_context["industry"]["name"]
        sub_industry = business_context["industry"]["sub_industry"]
        business_size = business_context["business_size"]["category"]
        org_role = business_context["user_role"]["organizational"]["id"]
        func_role = business_context["user_role"]["functional"]["id"]
        
        # Get detailed information
        industry_info = self.industry_classifier.get_industry_information(industry_id)
        size_info = self.business_size_analyzer.get_size_information(business_size)
        communication_strategy = self.role_recognizer.get_communication_strategy(org_role)
        
        # Generate adaptation strategy
        adaptation_strategy = {
            "content_adaptation": {
                "industry_focus": {
                    "primary_topics": industry_info.get("keywords", [])[:5],
                    "sub_industry_focus": sub_industry["name"] if sub_industry else None,
                    "industry_challenges": [
                        f"Addressing {industry_name} industry regulations and compliance requirements",
                        f"Managing {industry_name}-specific customer expectations",
                        f"Optimizing {industry_name} business processes and workflows",
                        f"Leveraging technology effectively in the {industry_name} sector",
                        f"Staying competitive in the evolving {industry_name} landscape"
                    ]
                },
                "business_size_adaptation": {
                    "resource_considerations": size_info.get("challenges", []),
                    "opportunity_focus": size_info.get("opportunities", []),
                    "implementation_approach": self._generate_implementation_approach(business_size)
                },
                "role_based_communication": {
                    "content_focus": communication_strategy.get("content_focus", []),
                    "presentation_style": communication_strategy.get("presentation_style", []),
                    "language_patterns": communication_strategy.get("language_patterns", [])
                }
            },
            "feature_adaptation": {
                "recommended_capabilities": self._generate_recommended_capabilities(industry_id, business_size, org_role),
                "interface_customization": self._generate_interface_recommendations(org_role, func_role),
                "integration_priorities": self._generate_integration_priorities(industry_id, business_size)
            },
            "engagement_strategy": {
                "value_proposition_focus": self._generate_value_proposition_focus(industry_id, business_size, org_role),
                "roi_emphasis": self._generate_roi_emphasis(org_role, business_size),
                "trust_building_approach": self._generate_trust_building_approach(industry_id, org_role)
            }
        }
        
        return adaptation_strategy
    
    def _generate_implementation_approach(self, business_size: str) -> List[str]:
        """
        Generate implementation approach recommendations based on business size.
        
        Args:
            business_size: The business size category
            
        Returns:
            List[str]: Implementation approach recommendations
        """
        if business_size == "small":
            return [
                "Simplified deployment with minimal IT requirements",
                "Phased implementation with quick initial value delivery",
                "Self-service configuration options",
                "Minimal customization to reduce complexity",
                "Cloud-based deployment to minimize infrastructure needs"
            ]
        elif business_size == "medium":
            return [
                "Balanced approach with moderate customization",
                "Departmental rollout strategy",
                "Integration with core existing systems",
                "Hybrid configuration (self-service with support options)",
                "Scalable implementation that grows with the business"
            ]
        else:  # enterprise
            return [
                "Comprehensive implementation with extensive customization",
                "Enterprise-wide deployment strategy",
                "Deep integration with existing technology ecosystem",
                "Professional services-led implementation",
                "Multi-phase rollout with detailed change management"
            ]
    
    def _generate_recommended_capabilities(self, industry: str, business_size: str, role: str) -> List[str]:
        """
        Generate recommended capabilities based on business context.
        
        Args:
            industry: The industry ID
            business_size: The business size category
            role: The organizational role ID
            
        Returns:
            List[str]: Recommended capabilities
        """
        # Base capabilities for all contexts
        base_capabilities = [
            "Natural language interaction",
            "Business context awareness",
            "Self-marketing capabilities",
            "Integration with existing systems"
        ]
        
        # Industry-specific capabilities
        industry_capabilities = {
            "retail": [
                "Customer behavior analysis",
                "Inventory optimization",
                "Pricing strategy recommendations",
                "Omnichannel experience coordination"
            ],
            "healthcare": [
                "HIPAA-compliant data handling",
                "Patient engagement optimization",
                "Clinical workflow integration",
                "Healthcare regulation monitoring"
            ],
            "finance": [
                "Financial data analysis",
                "Regulatory compliance monitoring",
                "Risk assessment",
                "Investment performance tracking"
            ],
            "manufacturing": [
                "Supply chain optimization",
                "Production efficiency analysis",
                "Quality control monitoring",
                "Equipment maintenance prediction"
            ],
            "technology": [
                "Development workflow integration",
                "Technical documentation assistance",
                "Code quality analysis",
                "Technology trend monitoring"
            ]
        }
        
        # Size-specific capabilities
        size_capabilities = {
            "small": [
                "Cost-effective resource allocation",
                "Multi-function capabilities for limited staff",
                "Simplified reporting and analytics",
                "Quick-start templates and workflows"
            ],
            "medium": [
                "Department coordination tools",
                "Scalable workflow management",
                "Growth planning and forecasting",
                "Team collaboration features"
            ],
            "enterprise": [
                "Enterprise-wide data integration",
                "Advanced analytics and reporting",
                "Multi-location coordination",
                "Governance and compliance tools"
            ]
        }
        
        # Role-specific capabilities
        role_capabilities = {
            "executive": [
                "Strategic decision support",
                "Executive dashboard",
                "Competitive intelligence",
                "Performance overview"
            ],
            "manager": [
                "Team performance tracking",
                "Resource allocation tools",
                "Project management features",
                "Operational efficiency analysis"
            ],
            "specialist": [
                "Detailed technical tools",
                "Domain-specific analysis",
                "Process automation",
                "Knowledge management"
            ]
        }
        
        # Combine capabilities based on context
        recommended_capabilities = base_capabilities.copy()
        
        # Add industry-specific capabilities
        if industry in industry_capabilities:
            recommended_capabilities.extend(industry_capabilities[industry])
        else:
            recommended_capabilities.extend(industry_capabilities["technology"])
        
        # Add size-specific capabilities
        if business_size in size_capabilities:
            recommended_capabilities.extend(size_capabilities[business_size])
        else:
            recommended_capabilities.extend(size_capabilities["medium"])
        
        # Add role-specific capabilities
        if role in role_capabilities:
            recommended_capabilities.extend(role_capabilities[role])
        else:
            recommended_capabilities.extend(role_capabilities["manager"])
        
        return recommended_capabilities
    
    def _generate_interface_recommendations(self, org_role: str, func_role: str) -> Dict:
        """
        Generate interface customization recommendations based on user role.
        
        Args:
            org_role: The organizational role ID
            func_role: The functional role ID
            
        Returns:
            Dict: Interface customization recommendations
        """
        # Base interface recommendations
        interface_recommendations = {
            "layout": "Standard dashboard layout with customizable widgets",
            "data_visualization": "Balanced mix of charts, tables, and summary metrics",
            "navigation": "Context-aware navigation with recent items",
            "interaction_mode": "Conversational with option for structured inputs",
            "notification_style": "Balanced notification frequency and detail"
        }
        
        # Organizational role-specific adjustments
        if org_role == "executive":
            interface_recommendations.update({
                "layout": "Executive dashboard with high-level KPIs and strategic insights",
                "data_visualization": "Visual-focused with emphasis on trends and comparisons",
                "navigation": "Simplified navigation with focus on strategic areas",
                "interaction_mode": "Concise interactions with option for detailed exploration",
                "notification_style": "High-priority notifications only with executive summaries"
            })
        elif org_role == "specialist":
            interface_recommendations.update({
                "layout": "Detailed technical dashboard with comprehensive data access",
                "data_visualization": "Detailed data tables with technical visualizations",
                "navigation": "Deep navigation structure with technical categorization",
                "interaction_mode": "Technical query capability with specialized terminology",
                "notification_style": "Detailed notifications with technical specifics"
            })
        
        # Functional role-specific adjustments
        if func_role == "technology":
            interface_recommendations.update({
                "technical_features": "Code integration, API access, and technical documentation",
                "terminology": "Technical terminology and industry-standard nomenclature",
                "tools_integration": "Development environment and technical tool integrations"
            })
        elif func_role == "marketing":
            interface_recommendations.update({
                "technical_features": "Campaign analytics, content management, and audience insights",
                "terminology": "Marketing terminology and metrics",
                "tools_integration": "Marketing platform and analytics tool integrations"
            })
        elif func_role == "sales":
            interface_recommendations.update({
                "technical_features": "Pipeline management, customer tracking, and deal analytics",
                "terminology": "Sales terminology and metrics",
                "tools_integration": "CRM and sales tool integrations"
            })
        elif func_role == "finance":
            interface_recommendations.update({
                "technical_features": "Financial reporting, budget tracking, and forecast modeling",
                "terminology": "Financial terminology and metrics",
                "tools_integration": "Accounting system and financial tool integrations"
            })
        else:
            interface_recommendations.update({
                "technical_features": "Role-specific tools and analytics",
                "terminology": "Industry-standard terminology",
                "tools_integration": "Common business tool integrations"
            })
        
        return interface_recommendations
    
    def _generate_integration_priorities(self, industry: str, business_size: str) -> List[str]:
        """
        Generate integration priorities based on industry and business size.
        
        Args:
            industry: The industry ID
            business_size: The business size category
            
        Returns:
            List[str]: Integration priorities
        """
        # Base integration priorities
        base_priorities = [
            "Email and communication systems",
            "Calendar and scheduling tools",
            "Document management systems"
        ]
        
        # Industry-specific priorities
        industry_priorities = {
            "retail": [
                "Point of sale (POS) systems",
                "Inventory management systems",
                "E-commerce platforms",
                "Customer relationship management (CRM)"
            ],
            "healthcare": [
                "Electronic health record (EHR) systems",
                "Practice management software",
                "Patient portal systems",
                "Medical billing systems"
            ],
            "finance": [
                "Financial management systems",
                "Trading platforms",
                "Risk management tools",
                "Compliance monitoring systems"
            ],
            "manufacturing": [
                "Enterprise resource planning (ERP) systems",
                "Manufacturing execution systems (MES)",
                "Supply chain management tools",
                "Quality management systems"
            ],
            "technology": [
                "Development environments",
                "Project management tools",
                "Version control systems",
                "Continuous integration/deployment tools"
            ]
        }
        
        # Size-specific priorities
        size_priorities = {
            "small": [
                "All-in-one business management tools",
                "Cloud-based productivity suites",
                "Simple accounting systems"
            ],
            "medium": [
                "Department-specific software systems",
                "Business intelligence tools",
                "Team collaboration platforms"
            ],
            "enterprise": [
                "Enterprise resource planning (ERP) systems",
                "Data warehouse and analytics platforms",
                "Identity and access management systems",
                "Enterprise content management systems"
            ]
        }
        
        # Combine priorities based on context
        integration_priorities = base_priorities.copy()
        
        # Add industry-specific priorities
        if industry in industry_priorities:
            integration_priorities.extend(industry_priorities[industry])
        else:
            integration_priorities.extend(industry_priorities["technology"])
        
        # Add size-specific priorities
        if business_size in size_priorities:
            integration_priorities.extend(size_priorities[business_size])
        else:
            integration_priorities.extend(size_priorities["medium"])
        
        return integration_priorities
    
    def _generate_value_proposition_focus(self, industry: str, business_size: str, role: str) -> List[str]:
        """
        Generate value proposition focus areas based on business context.
        
        Args:
            industry: The industry ID
            business_size: The business size category
            role: The organizational role ID
            
        Returns:
            List[str]: Value proposition focus areas
        """
        # Industry-specific value propositions
        industry_value_props = {
            "retail": [
                "Increased customer engagement and loyalty",
                "Optimized inventory management and reduced costs",
                "Enhanced omnichannel customer experience",
                "Data-driven merchandising and pricing decisions"
            ],
            "healthcare": [
                "Improved patient outcomes and satisfaction",
                "Enhanced operational efficiency and reduced costs",
                "Streamlined compliance with healthcare regulations",
                "Better coordination of care across providers"
            ],
            "finance": [
                "Enhanced risk management and compliance",
                "Improved customer financial insights",
                "Streamlined financial operations and reporting",
                "Data-driven investment and lending decisions"
            ],
            "manufacturing": [
                "Optimized production efficiency and reduced waste",
                "Enhanced supply chain visibility and resilience",
                "Improved quality control and reduced defects",
                "Predictive maintenance to minimize downtime"
            ],
            "technology": [
                "Accelerated development cycles and innovation",
                "Improved code quality and reduced technical debt",
                "Enhanced collaboration across development teams",
                "Better alignment of technology with business objectives"
            ]
        }
        
        # Size-specific value propositions
        size_value_props = {
            "small": [
                "Cost-effective operations with minimal overhead",
                "Ability to compete with larger businesses",
                "Maximized productivity with limited resources",
                "Simplified management of multiple business functions"
            ],
            "medium": [
                "Scalable growth without proportional cost increases",
                "Improved coordination across departments",
                "Enhanced ability to adapt to market changes",
                "Better visibility into business operations"
            ],
            "enterprise": [
                "Enterprise-wide consistency and standardization",
                "Improved governance and risk management",
                "Enhanced coordination across locations and divisions",
                "Data-driven strategic decision making"
            ]
        }
        
        # Role-specific value propositions
        role_value_props = {
            "executive": [
                "Strategic competitive advantage",
                "Improved organizational performance and growth",
                "Enhanced decision-making with strategic insights",
                "Reduced organizational risk and improved governance"
            ],
            "manager": [
                "Improved team productivity and performance",
                "Better resource allocation and utilization",
                "Enhanced visibility into operations",
                "Streamlined processes and reduced manual work"
            ],
            "specialist": [
                "Automation of routine tasks",
                "Enhanced technical capabilities and tools",
                "Improved quality and consistency of work",
                "Access to specialized knowledge and best practices"
            ]
        }
        
        # Select value propositions based on context
        value_proposition_focus = []
        
        # Add industry-specific value propositions
        if industry in industry_value_props:
            value_proposition_focus.extend(industry_value_props[industry][:2])
        else:
            value_proposition_focus.extend(industry_value_props["technology"][:2])
        
        # Add size-specific value propositions
        if business_size in size_value_props:
            value_proposition_focus.extend(size_value_props[business_size][:2])
        else:
            value_proposition_focus.extend(size_value_props["medium"][:2])
        
        # Add role-specific value propositions
        if role in role_value_props:
            value_proposition_focus.extend(role_value_props[role][:2])
        else:
            value_proposition_focus.extend(role_value_props["manager"][:2])
        
        return value_proposition_focus
    
    def _generate_roi_emphasis(self, role: str, business_size: str) -> List[str]:
        """
        Generate ROI emphasis areas based on role and business size.
        
        Args:
            role: The organizational role ID
            business_size: The business size category
            
        Returns:
            List[str]: ROI emphasis areas
        """
        # Role-specific ROI emphasis
        role_roi = {
            "executive": [
                "Long-term strategic value and competitive positioning",
                "Overall business growth and market share impact",
                "Organizational efficiency and cost reduction",
                "Risk mitigation and compliance benefits"
            ],
            "manager": [
                "Team productivity improvements",
                "Process efficiency and time savings",
                "Resource utilization optimization",
                "Quality improvements and error reduction"
            ],
            "specialist": [
                "Task automation and time savings",
                "Quality improvements and error reduction",
                "Technical capability enhancements",
                "Professional development and knowledge access"
            ]
        }
        
        # Size-specific ROI emphasis
        size_roi = {
            "small": [
                "Quick time-to-value with minimal investment",
                "Cost-effective operations with limited resources",
                "Competitive capabilities without enterprise budgets",
                "Flexibility to adapt to changing business needs"
            ],
            "medium": [
                "Scalable growth without proportional cost increases",
                "Improved coordination and reduced operational friction",
                "Enhanced capabilities to compete with larger businesses",
                "Balanced investment with measurable returns"
            ],
            "enterprise": [
                "Enterprise-wide efficiency and standardization",
                "Significant cost reduction at scale",
                "Strategic advantage through advanced capabilities",
                "Risk reduction and compliance benefits"
            ]
        }
        
        # Combine ROI emphasis based on context
        roi_emphasis = []
        
        # Add role-specific ROI emphasis
        if role in role_roi:
            roi_emphasis.extend(role_roi[role][:3])
        else:
            roi_emphasis.extend(role_roi["manager"][:3])
        
        # Add size-specific ROI emphasis
        if business_size in size_roi:
            roi_emphasis.extend(size_roi[business_size][:3])
        else:
            roi_emphasis.extend(size_roi["medium"][:3])
        
        return roi_emphasis
    
    def _generate_trust_building_approach(self, industry: str, role: str) -> Dict:
        """
        Generate trust building approach based on industry and role.
        
        Args:
            industry: The industry ID
            role: The organizational role ID
            
        Returns:
            Dict: Trust building approach
        """
        # Base trust building elements
        trust_approach = {
            "security_emphasis": [
                "Data encryption and protection",
                "Access controls and authentication",
                "Regular security audits and updates"
            ],
            "privacy_emphasis": [
                "Data minimization principles",
                "User control over data",
                "Transparent data usage policies"
            ],
            "reliability_emphasis": [
                "System uptime and availability",
                "Performance consistency",
                "Quality assurance processes"
            ]
        }
        
        # Industry-specific trust elements
        industry_trust = {
            "healthcare": {
                "security_emphasis": [
                    "HIPAA-compliant security measures",
                    "Protected health information (PHI) safeguards",
                    "Healthcare-specific access controls"
                ],
                "privacy_emphasis": [
                    "Patient data protection and consent management",
                    "Healthcare privacy regulation compliance",
                    "Strict data sharing controls"
                ],
                "compliance_emphasis": [
                    "Healthcare regulatory compliance",
                    "Audit trail for all PHI access",
                    "Regular compliance verification"
                ]
            },
            "finance": {
                "security_emphasis": [
                    "Financial-grade security protocols",
                    "Fraud detection and prevention",
                    "Multi-factor authentication"
                ],
                "privacy_emphasis": [
                    "Financial data protection",
                    "Strict data access controls",
                    "Transparent data usage policies"
                ],
                "compliance_emphasis": [
                    "Financial regulatory compliance",
                    "Audit trails for all transactions",
                    "Regular compliance verification"
                ]
            },
            "retail": {
                "security_emphasis": [
                    "Payment card industry (PCI) compliance",
                    "Customer data protection",
                    "Secure e-commerce transactions"
                ],
                "privacy_emphasis": [
                    "Customer privacy protection",
                    "Transparent data collection policies",
                    "Opt-in consent for marketing"
                ],
                "customer_trust_emphasis": [
                    "Consistent customer experience",
                    "Transparent pricing and policies",
                    "Reliable service delivery"
                ]
            }
        }
        
        # Role-specific trust elements
        role_trust = {
            "executive": {
                "strategic_emphasis": [
                    "Long-term partnership approach",
                    "Strategic alignment with business goals",
                    "Executive-level support and accountability"
                ],
                "governance_emphasis": [
                    "Clear governance and oversight",
                    "Risk management framework",
                    "Executive reporting and visibility"
                ]
            },
            "specialist": {
                "technical_emphasis": [
                    "Technical reliability and performance",
                    "Integration with existing tools",
                    "Technical support and expertise"
                ],
                "transparency_emphasis": [
                    "Technical documentation and specifications",
                    "Clear explanation of capabilities and limitations",
                    "Transparent technical processes"
                ]
            }
        }
        
        # Update trust approach based on industry
        if industry in industry_trust:
            for key, value in industry_trust[industry].items():
                if key in trust_approach:
                    trust_approach[key] = value
                else:
                    trust_approach[key] = value
        
        # Update trust approach based on role
        if role in role_trust:
            for key, value in role_trust[role].items():
                if key in trust_approach:
                    trust_approach[key] = value
                else:
                    trust_approach[key] = value
        
        return trust_approach


# Example usage
if __name__ == "__main__":
    adapter = BusinessContextAdapter()
    
    # Analyze business context
    context = adapter.analyze_business_context(
        business_description="We are a mid-sized retail company specializing in electronics and home appliances with both physical stores and an e-commerce platform.",
        job_title="Marketing Director",
        employees_count=120,
        annual_revenue=25000000,
        additional_info={
            "keywords": ["retail", "electronics", "e-commerce", "omnichannel"],
            "role_info": "Responsible for digital marketing strategy and brand development",
            "industry_metrics": {"locations": 8}
        }
    )
    
    print("Business Context Analysis:")
    print(f"Industry: {context['industry']['name']}")
    if context['industry']['sub_industry']:
        print(f"Sub-Industry: {context['industry']['sub_industry']['name']}")
    print(f"Business Size: {context['business_size']['category'].capitalize()}")
    print(f"Organizational Role: {context['user_role']['organizational']['name']}")
    print(f"Functional Role: {context['user_role']['functional']['name']}")
    
    # Generate adaptation strategy
    strategy = adapter.generate_adaptation_strategy(context)
    
    print("\nAdaptation Strategy Highlights:")
    print("\nValue Proposition Focus:")
    for prop in strategy['engagement_strategy']['value_proposition_focus'][:3]:
        print(f"- {prop}")
    
    print("\nRecommended Capabilities:")
    for capability in strategy['feature_adaptation']['recommended_capabilities'][:3]:
        print(f"- {capability}")
    
    print("\nCommunication Approach:")
    for style in strategy['content_adaptation']['role_based_communication']['presentation_style'][:3]:
        print(f"- {style}")
