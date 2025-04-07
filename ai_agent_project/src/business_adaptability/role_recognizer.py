"""
Role Recognizer Module

This module identifies user roles and tailors interactions accordingly.
"""

import json
import re
from typing import Dict, List, Optional, Tuple

class RoleRecognizer:
    """
    Identifies user roles and tailors interactions based on role.
    """
    
    def __init__(self, role_data_path: str = "role_data.json"):
        """
        Initialize the Role Recognizer.
        
        Args:
            role_data_path: Path to the role data file
        """
        self.role_data_path = role_data_path
        self.role_data = self._load_role_data()
        
    def _load_role_data(self) -> Dict:
        """
        Load the role data from file.
        
        Returns:
            Dict: The role data
        """
        try:
            with open(self.role_data_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default role data if file not found or invalid
            return self._create_default_role_data()
    
    def _create_default_role_data(self) -> Dict:
        """
        Create default role data with classifications and characteristics.
        
        Returns:
            Dict: Default role data
        """
        default_role_data = {
            "organizational_roles": {
                "executive": {
                    "name": "Executive",
                    "description": "Senior leadership responsible for strategic decisions and overall direction.",
                    "keywords": [
                        "CEO", "CFO", "CTO", "CIO", "COO", "CMO", "CHRO", "executive", "chief", 
                        "president", "vice president", "VP", "director", "head", "founder", 
                        "owner", "partner", "board member", "chairman", "chairwoman"
                    ],
                    "interests": [
                        "strategic planning", "business growth", "market positioning", 
                        "competitive advantage", "financial performance", "organizational development",
                        "risk management", "innovation strategy", "leadership"
                    ],
                    "communication_preferences": {
                        "style": "concise, strategic, business-focused",
                        "detail_level": "high-level with key details",
                        "data_focus": "outcomes, ROI, strategic impact",
                        "time_sensitivity": "highly time-sensitive, respect for limited availability"
                    }
                },
                "manager": {
                    "name": "Manager",
                    "description": "Mid-level leadership responsible for team performance and operational execution.",
                    "keywords": [
                        "manager", "supervisor", "team lead", "project manager", "department head",
                        "coordinator", "administrator", "lead", "senior", "principal"
                    ],
                    "interests": [
                        "team productivity", "process improvement", "resource allocation",
                        "performance metrics", "project management", "staff development",
                        "operational efficiency", "budget management", "team collaboration"
                    ],
                    "communication_preferences": {
                        "style": "practical, action-oriented, solution-focused",
                        "detail_level": "balanced with actionable details",
                        "data_focus": "performance metrics, efficiency gains, resource utilization",
                        "time_sensitivity": "moderate, focused on operational timelines"
                    }
                },
                "specialist": {
                    "name": "Specialist",
                    "description": "Individual contributor with specialized expertise in a specific domain.",
                    "keywords": [
                        "specialist", "expert", "analyst", "engineer", "developer", "designer",
                        "consultant", "technician", "associate", "professional", "advisor",
                        "representative", "agent", "coordinator"
                    ],
                    "interests": [
                        "technical details", "domain expertise", "best practices", "tools and technologies",
                        "skill development", "problem solving", "technical challenges", "innovation",
                        "efficiency improvements", "professional development"
                    ],
                    "communication_preferences": {
                        "style": "detailed, technical, evidence-based",
                        "detail_level": "comprehensive with technical specifics",
                        "data_focus": "technical metrics, detailed analysis, implementation specifics",
                        "time_sensitivity": "variable, focused on task completion"
                    }
                }
            },
            "functional_roles": {
                "technology": {
                    "name": "Technology",
                    "description": "Roles focused on technology development, implementation, and management.",
                    "keywords": [
                        "developer", "engineer", "programmer", "architect", "administrator",
                        "technician", "analyst", "IT", "technical", "software", "hardware",
                        "network", "database", "security", "support", "DevOps", "QA"
                    ],
                    "interests": [
                        "technology stack", "development methodologies", "technical specifications",
                        "system architecture", "code quality", "performance optimization",
                        "security considerations", "integration capabilities", "scalability"
                    ]
                },
                "marketing": {
                    "name": "Marketing",
                    "description": "Roles focused on promoting products/services and building brand awareness.",
                    "keywords": [
                        "marketing", "brand", "advertising", "communications", "PR", "public relations",
                        "content", "social media", "digital", "campaign", "market research", "SEO",
                        "growth", "acquisition", "engagement", "retention", "conversion"
                    ],
                    "interests": [
                        "customer acquisition", "brand positioning", "campaign performance",
                        "market trends", "customer engagement", "content strategy",
                        "conversion optimization", "audience targeting", "marketing analytics"
                    ]
                },
                "sales": {
                    "name": "Sales",
                    "description": "Roles focused on selling products/services and managing customer relationships.",
                    "keywords": [
                        "sales", "account", "business development", "customer success", "relationship",
                        "revenue", "deal", "pipeline", "forecast", "quota", "prospect", "lead",
                        "opportunity", "client", "customer"
                    ],
                    "interests": [
                        "sales process", "customer acquisition", "deal closing", "revenue growth",
                        "customer relationships", "competitive positioning", "value proposition",
                        "pricing strategy", "sales enablement", "customer success"
                    ]
                },
                "finance": {
                    "name": "Finance",
                    "description": "Roles focused on financial management, analysis, and reporting.",
                    "keywords": [
                        "finance", "accounting", "financial", "budget", "forecast", "analysis",
                        "controller", "treasurer", "auditor", "tax", "investment", "capital",
                        "revenue", "expense", "profit", "loss", "cash flow", "balance sheet"
                    ],
                    "interests": [
                        "financial performance", "cost management", "budget planning",
                        "financial reporting", "risk assessment", "investment analysis",
                        "cash flow management", "profitability analysis", "financial controls"
                    ]
                },
                "operations": {
                    "name": "Operations",
                    "description": "Roles focused on day-to-day business operations and process management.",
                    "keywords": [
                        "operations", "process", "production", "logistics", "supply chain",
                        "procurement", "inventory", "quality", "facilities", "manufacturing",
                        "distribution", "warehouse", "fulfillment", "service delivery"
                    ],
                    "interests": [
                        "operational efficiency", "process optimization", "quality control",
                        "resource utilization", "supply chain management", "inventory management",
                        "service delivery", "operational costs", "compliance", "risk management"
                    ]
                },
                "human_resources": {
                    "name": "Human Resources",
                    "description": "Roles focused on people management, talent development, and organizational culture.",
                    "keywords": [
                        "HR", "human resources", "people", "talent", "recruitment", "hiring",
                        "training", "development", "compensation", "benefits", "culture",
                        "employee", "workforce", "staff", "personnel", "organizational"
                    ],
                    "interests": [
                        "talent acquisition", "employee development", "performance management",
                        "compensation strategy", "employee engagement", "organizational culture",
                        "workforce planning", "compliance", "employee experience", "retention"
                    ]
                }
            },
            "industry_specific_roles": {
                "healthcare": {
                    "clinical": {
                        "name": "Clinical",
                        "description": "Healthcare professionals directly involved in patient care.",
                        "keywords": [
                            "doctor", "physician", "nurse", "practitioner", "therapist", "clinician",
                            "medical", "clinical", "patient care", "treatment", "diagnosis"
                        ],
                        "interests": [
                            "patient outcomes", "clinical workflows", "treatment protocols",
                            "medical records", "patient management", "care coordination",
                            "clinical decision support", "evidence-based practice"
                        ]
                    },
                    "administrative": {
                        "name": "Healthcare Administration",
                        "description": "Professionals managing healthcare operations and compliance.",
                        "keywords": [
                            "administrator", "coordinator", "director", "manager", "compliance",
                            "billing", "coding", "records", "regulatory", "operations"
                        ],
                        "interests": [
                            "regulatory compliance", "operational efficiency", "patient satisfaction",
                            "healthcare costs", "facility management", "staff coordination",
                            "healthcare policy", "quality metrics", "accreditation"
                        ]
                    }
                },
                "finance": {
                    "investment": {
                        "name": "Investment Professional",
                        "description": "Professionals managing investments and financial assets.",
                        "keywords": [
                            "investment", "portfolio", "asset", "wealth", "advisor", "banker",
                            "trader", "analyst", "fund", "capital", "securities"
                        ],
                        "interests": [
                            "investment performance", "market analysis", "portfolio management",
                            "risk assessment", "asset allocation", "client relationships",
                            "financial planning", "wealth management", "market trends"
                        ]
                    },
                    "banking": {
                        "name": "Banking Professional",
                        "description": "Professionals working in banking and financial services.",
                        "keywords": [
                            "banker", "teller", "loan", "credit", "branch", "banking",
                            "account", "deposit", "mortgage", "financial services"
                        ],
                        "interests": [
                            "customer service", "account management", "lending practices",
                            "banking regulations", "financial products", "customer acquisition",
                            "risk management", "digital banking", "branch operations"
                        ]
                    }
                },
                "retail": {
                    "merchandising": {
                        "name": "Merchandising Professional",
                        "description": "Professionals managing product selection, pricing, and presentation.",
                        "keywords": [
                            "merchandiser", "buyer", "product", "assortment", "category",
                            "pricing", "promotion", "inventory", "retail", "purchasing"
                        ],
                        "interests": [
                            "product selection", "inventory management", "pricing strategy",
                            "product placement", "seasonal planning", "vendor relationships",
                            "sales performance", "market trends", "customer preferences"
                        ]
                    },
                    "store_operations": {
                        "name": "Store Operations Professional",
                        "description": "Professionals managing retail store operations and customer experience.",
                        "keywords": [
                            "store", "retail", "shop", "manager", "associate", "sales floor",
                            "customer service", "operations", "cashier", "floor"
                        ],
                        "interests": [
                            "store performance", "customer experience", "staff management",
                            "visual merchandising", "loss prevention", "sales targets",
                            "operational efficiency", "customer service", "store layout"
                        ]
                    }
                }
            },
            "communication_strategies": {
                "executive": {
                    "content_focus": [
                        "Strategic impact and business outcomes",
                        "ROI and financial implications",
                        "Competitive advantage and market positioning",
                        "Risk assessment and mitigation",
                        "High-level implementation considerations"
                    ],
                    "presentation_style": [
                        "Begin with key conclusions and recommendations",
                        "Use executive summaries with clear, actionable insights",
                        "Include visual representations of data and trends",
                        "Provide strategic context for recommendations",
                        "Offer clear next steps and decision points"
                    ],
                    "language_patterns": [
                        "Strategic, forward-looking terminology",
                        "Business outcome-focused language",
                        "Confident, decisive phrasing",
                        "Industry-specific executive terminology",
                        "Concise, impactful statements"
                    ]
                },
                "manager": {
                    "content_focus": [
                        "Operational implementation details",
                        "Team impact and resource requirements",
                        "Performance metrics and measurement",
                        "Process improvements and efficiency gains",
                        "Timeline and milestone planning"
                    ],
                    "presentation_style": [
                        "Balance strategic context with tactical details",
                        "Include implementation roadmaps and timelines",
                        "Provide team-level impact analysis",
                        "Offer resource allocation recommendations",
                        "Include change management considerations"
                    ],
                    "language_patterns": [
                        "Action-oriented, practical terminology",
                        "Team and resource-focused language",
                        "Process and implementation phrasing",
                        "Balanced technical and business terminology",
                        "Clear direction and guidance statements"
                    ]
                },
                "specialist": {
                    "content_focus": [
                        "Technical details and specifications",
                        "Implementation methodologies and best practices",
                        "Tool-specific features and capabilities",
                        "Technical challenges and solutions",
                        "Detailed performance metrics and analysis"
                    ],
                    "presentation_style": [
                        "Provide comprehensive technical details",
                        "Include technical diagrams and specifications",
                        "Reference industry standards and best practices",
                        "Offer detailed implementation guidance",
                        "Include technical comparisons and benchmarks"
                    ],
                    "language_patterns": [
                        "Technically precise terminology",
                        "Domain-specific jargon and acronyms",
                        "Detailed, specific descriptions",
                        "Evidence-based, analytical phrasing",
                        "Implementation-focused language"
                    ]
                }
            }
        }
        
        # Save the default role data
        with open(self.role_data_path, 'w') as f:
            json.dump(default_role_data, f, indent=4)
            
        return default_role_data
    
    def recognize_role(self, 
                      job_title: str,
                      additional_info: Optional[str] = None,
                      industry: Optional[str] = None) -> Dict:
        """
        Recognize the user's role based on job title and additional information.
        
        Args:
            job_title: The user's job title
            additional_info: Optional additional information about the user's role
            industry: Optional industry context to consider industry-specific roles
            
        Returns:
            Dict: Role recognition results
        """
        # Normalize inputs to lowercase
        job_title_lower = job_title.lower()
        additional_info_lower = additional_info.lower() if additional_info else ""
        industry_lower = industry.lower() if industry else ""
        
        # Combined text for analysis
        combined_text = f"{job_title_lower} {additional_info_lower}"
        
        # Initialize scores
        organizational_role_scores = {}
        functional_role_scores = {}
        industry_role_scores = {}
        
        # Score organizational roles
        for role_id, role_info in self.role_data["organizational_roles"].items():
            score = self._calculate_role_score(combined_text, role_info["keywords"])
            if score > 0:
                organizational_role_scores[role_id] = score
        
        # Score functional roles
        for role_id, role_info in self.role_data["functional_roles"].items():
            score = self._calculate_role_score(combined_text, role_info["keywords"])
            if score > 0:
                functional_role_scores[role_id] = score
        
        # Score industry-specific roles if industry is provided
        if industry and industry_lower in self.role_data["industry_specific_roles"]:
            for role_id, role_info in self.role_data["industry_specific_roles"][industry_lower].items():
                score = self._calculate_role_score(combined_text, role_info["keywords"])
                if score > 0:
                    industry_role_scores[role_id] = score
        
        # Determine primary organizational role
        primary_org_role = self._get_highest_scoring_role(
            organizational_role_scores, 
            self.role_data["organizational_roles"],
            default_role="manager"
        )
        
        # Determine primary functional role
        primary_func_role = self._get_highest_scoring_role(
            functional_role_scores, 
            self.role_data["functional_roles"],
            default_role="technology"
        )
        
        # Determine primary industry-specific role if applicable
        primary_industry_role = None
        if industry and industry_lower in self.role_data["industry_specific_roles"] and industry_role_scores:
            primary_industry_role = self._get_highest_scoring_role(
                industry_role_scores, 
                self.role_data["industry_specific_roles"][industry_lower]
            )
        
        # Get communication strategy for the primary organizational role
        communication_strategy = self.role_data["communication_strategies"].get(
            primary_org_role["id"],
            self.role_data["communication_strategies"]["manager"]  # Default to manager if not found
        )
        
        # Compile results
        recognition_results = {
            "organizational_role": primary_org_role,
            "functional_role": primary_func_role,
            "industry_specific_role": primary_industry_role,
            "communication_strategy": communication_strategy,
            "all_matches": {
                "organizational_roles": {
                    role_id: {
                        "name": self.role_data["organizational_roles"][role_id]["name"],
                        "score": score
                    }
                    for role_id, score in organizational_role_scores.items()
                },
                "functional_roles": {
                    role_id: {
                        "name": self.role_data["functional_roles"][role_id]["name"],
                        "score": score
                    }
                    for role_id, score in functional_role_scores.items()
                }
            }
        }
        
        # Add industry-specific roles if applicable
        if industry and industry_lower in self.role_data["industry_specific_roles"] and industry_role_scores:
            recognition_results["all_matches"]["industry_specific_roles"] = {
                role_id: {
                    "name": self.role_data["industry_specific_roles"][industry_lower][role_id]["name"],
                    "score": score
                }
                for role_id, score in industry_role_scores.items()
            }
        
        return recognition_results
    
    def _calculate_role_score(self, text: str, keywords: List[str]) -> float:
        """
        Calculate a score for a role based on keyword matches.
        
        Args:
            text: The text to analyze
            keywords: List of keywords to match
            
        Returns:
            float: The calculated score
        """
        score = 0
        
        for keyword in keywords:
            # Count occurrences of the keyword
            count = len(re.findall(r'\b' + re.escape(keyword.lower()) + r'\b', text))
            if count > 0:
                # Add to score based on occurrence count and keyword specificity
                # More specific (longer) keywords get higher weight
                keyword_weight = 0.5 + (len(keyword) / 20)  # Base weight plus length factor
                score += count * keyword_weight
        
        return score
    
    def _get_highest_scoring_role(self, 
                                 role_scores: Dict[str, float], 
                                 role_data: Dict,
                                 default_role: Optional[str] = None) -> Dict:
        """
        Get the highest scoring role from a set of scores.
        
        Args:
            role_scores: Dictionary of role IDs and their scores
            role_data: Dictionary of role information
            default_role: Optional default role ID if no scores are available
            
        Returns:
            Dict: Information about the highest scoring role
        """
        if not role_scores:
            # No matches found, use default role if provided
            if default_role and default_role in role_data:
                return {
                    "id": default_role,
                    "name": role_data[default_role]["name"],
                    "description": role_data[default_role]["description"],
                    "confidence": 0
                }
            else:
                # Return empty result if no default provided
                return {
                    "id": "",
                    "name": "",
                    "description": "",
                    "confidence": 0
                }
        
        # Get the role with the highest score
        top_role_id = max(role_scores, key=role_scores.get)
        
        # Calculate confidence as a percentage of the total score
        total_score = sum(role_scores.values())
        confidence = (role_scores[top_role_id] / total_score) * 100 if total_score > 0 else 0
        
        return {
            "id": top_role_id,
            "name": role_data[top_role_id]["name"],
            "description": role_data[top_role_id]["description"],
            "confidence": round(confidence, 2)
        }
    
    def get_role_information(self, role_type: str, role_id: str, industry: Optional[str] = None) -> Dict:
        """
        Get detailed information about a specific role.
        
        Args:
            role_type: The type of role (organizational, functional, industry_specific)
            role_id: The role ID
            industry: Required for industry_specific roles
            
        Returns:
            Dict: Detailed role information
        """
        if role_type == "organizational" and role_id in self.role_data["organizational_roles"]:
            return self.role_data["organizational_roles"][role_id]
        elif role_type == "functional" and role_id in self.role_data["functional_roles"]:
            return self.role_data["functional_roles"][role_id]
        elif role_type == "industry_specific" and industry and industry in self.role_data["industry_specific_roles"]:
            if role_id in self.role_data["industry_specific_roles"][industry]:
                return self.role_data["industry_specific_roles"][industry][role_id]
        
        # Return empty dict if role not found
        return {}
    
    def get_communication_strategy(self, organizational_role: str) -> Dict:
        """
        Get the communication strategy for a specific organizational role.
        
        Args:
            organizational_role: The organizational role ID
            
        Returns:
            Dict: Communication strategy for the role
        """
        if organizational_role in self.role_data["communication_strategies"]:
            return self.role_data["communication_strategies"][organizational_role]
        else:
            # Default to manager if role not found
            return self.role_data["communication_strategies"]["manager"]
    
    def update_role_data(self, new_data: Dict) -> None:
        """
        Update the role data with new information.
        
        Args:
            new_data: New role data to add
        """
        # Merge new data with existing role data
        for category, category_data in new_data.items():
            if category in self.role_data:
                if isinstance(category_data, dict):
                    for key, value in category_data.items():
                        if key in self.role_data[category]:
                            # Update existing entry
                            if isinstance(value, dict) and isinstance(self.role_data[category][key], dict):
                                self.role_data[category][key].update(value)
                            else:
                                self.role_data[category][key] = value
                        else:
                            # Add new entry
                            self.role_data[category][key] = value
                elif isinstance(category_data, list):
                    # For list types, append new items
                    self.role_data[category].extend(category_data)
            else:
                # Add new category
                self.role_data[category] = category_data
                
        # Save updated role data
        with open(self.role_data_path, 'w') as f:
            json.dump(self.role_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    recognizer = RoleRecognizer()
    
    # Recognize a role
    recognition = recognizer.recognize_role(
        job_title="Marketing Director",
        additional_info="Responsible for digital marketing strategy and brand development",
        industry="retail"
    )
    
    print("Role Recognition:")
    print(f"Organizational Role: {recognition['organizational_role']['name']} "
          f"(Confidence: {recognition['organizational_role']['confidence']}%)")
    print(f"Functional Role: {recognition['functional_role']['name']} "
          f"(Confidence: {recognition['functional_role']['confidence']}%)")
    
    if recognition['industry_specific_role']:
        print(f"Industry-Specific Role: {recognition['industry_specific_role']['name']} "
              f"(Confidence: {recognition['industry_specific_role']['confidence']}%)")
    
    print("\nCommunication Strategy:")
    print("Content Focus:")
    for focus in recognition['communication_strategy']['content_focus'][:3]:
        print(f"- {focus}")
    
    print("\nPresentation Style:")
    for style in recognition['communication_strategy']['presentation_style'][:3]:
        print(f"- {style}")
