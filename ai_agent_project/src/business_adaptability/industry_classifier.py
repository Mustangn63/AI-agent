"""
Industry Classifier Module

This module identifies and categorizes the business industry based on provided information.
"""

import json
import re
from typing import Dict, List, Optional, Tuple

class IndustryClassifier:
    """
    Identifies and categorizes the business industry.
    """
    
    def __init__(self, industry_data_path: str = "industry_data.json"):
        """
        Initialize the Industry Classifier.
        
        Args:
            industry_data_path: Path to the industry data file
        """
        self.industry_data_path = industry_data_path
        self.industry_data = self._load_industry_data()
        
    def _load_industry_data(self) -> Dict:
        """
        Load the industry data from file.
        
        Returns:
            Dict: The industry data
        """
        try:
            with open(self.industry_data_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default industry data if file not found or invalid
            return self._create_default_industry_data()
    
    def _create_default_industry_data(self) -> Dict:
        """
        Create default industry data with classifications and keywords.
        
        Returns:
            Dict: Default industry data
        """
        default_industry_data = {
            "industries": {
                "retail": {
                    "name": "Retail",
                    "description": "Businesses that sell products directly to consumers.",
                    "keywords": [
                        "retail", "store", "shop", "e-commerce", "online store", "merchant", 
                        "seller", "sales", "consumer goods", "shopping", "marketplace"
                    ],
                    "sub_industries": {
                        "apparel": {
                            "name": "Apparel and Fashion",
                            "keywords": ["clothing", "fashion", "apparel", "shoes", "accessories", "jewelry", "wearables"]
                        },
                        "electronics": {
                            "name": "Electronics and Appliances",
                            "keywords": ["electronics", "appliances", "gadgets", "devices", "computers", "phones"]
                        },
                        "grocery": {
                            "name": "Grocery and Food Retail",
                            "keywords": ["grocery", "supermarket", "food", "beverage", "produce", "market"]
                        },
                        "home_goods": {
                            "name": "Home Goods and Furniture",
                            "keywords": ["furniture", "home goods", "decor", "housewares", "home improvement"]
                        }
                    }
                },
                "healthcare": {
                    "name": "Healthcare",
                    "description": "Organizations involved in providing medical services, products, or facilities.",
                    "keywords": [
                        "healthcare", "medical", "health", "hospital", "clinic", "patient", 
                        "doctor", "physician", "care", "wellness", "treatment"
                    ],
                    "sub_industries": {
                        "providers": {
                            "name": "Healthcare Providers",
                            "keywords": ["hospital", "clinic", "doctor", "physician", "nurse", "medical practice"]
                        },
                        "pharma": {
                            "name": "Pharmaceuticals",
                            "keywords": ["pharmaceutical", "pharma", "drug", "medication", "medicine", "biotech"]
                        },
                        "devices": {
                            "name": "Medical Devices",
                            "keywords": ["medical device", "equipment", "diagnostic", "implant", "prosthetic"]
                        },
                        "insurance": {
                            "name": "Health Insurance",
                            "keywords": ["health insurance", "payer", "coverage", "benefits", "claims"]
                        }
                    }
                },
                "finance": {
                    "name": "Finance",
                    "description": "Businesses that manage money, investments, and financial services.",
                    "keywords": [
                        "finance", "banking", "investment", "financial", "bank", "insurance", 
                        "wealth", "money", "capital", "loan", "credit", "asset"
                    ],
                    "sub_industries": {
                        "banking": {
                            "name": "Banking",
                            "keywords": ["bank", "banking", "savings", "checking", "deposit", "loan", "credit"]
                        },
                        "investment": {
                            "name": "Investment and Wealth Management",
                            "keywords": ["investment", "wealth", "asset", "portfolio", "fund", "stock", "bond"]
                        },
                        "insurance": {
                            "name": "Insurance",
                            "keywords": ["insurance", "insurer", "policy", "risk", "underwriting", "claim"]
                        },
                        "fintech": {
                            "name": "Financial Technology",
                            "keywords": ["fintech", "payment", "digital banking", "blockchain", "cryptocurrency"]
                        }
                    }
                },
                "manufacturing": {
                    "name": "Manufacturing",
                    "description": "Businesses that produce goods through processing, fabrication, or assembly.",
                    "keywords": [
                        "manufacturing", "factory", "production", "assembly", "fabrication", 
                        "industrial", "machinery", "processing", "materials", "goods"
                    ],
                    "sub_industries": {
                        "automotive": {
                            "name": "Automotive Manufacturing",
                            "keywords": ["automotive", "vehicle", "car", "auto parts", "automobile"]
                        },
                        "electronics": {
                            "name": "Electronics Manufacturing",
                            "keywords": ["electronics", "semiconductor", "circuit", "component", "device"]
                        },
                        "consumer_goods": {
                            "name": "Consumer Goods Manufacturing",
                            "keywords": ["consumer goods", "product", "packaged goods", "household"]
                        },
                        "industrial": {
                            "name": "Industrial Manufacturing",
                            "keywords": ["industrial", "machinery", "equipment", "heavy", "tool"]
                        }
                    }
                },
                "technology": {
                    "name": "Technology",
                    "description": "Businesses that develop or provide technology products and services.",
                    "keywords": [
                        "technology", "software", "IT", "tech", "digital", "computer", 
                        "internet", "web", "app", "cloud", "data", "platform"
                    ],
                    "sub_industries": {
                        "software": {
                            "name": "Software Development",
                            "keywords": ["software", "application", "app", "development", "programming", "SaaS"]
                        },
                        "hardware": {
                            "name": "Hardware and Devices",
                            "keywords": ["hardware", "device", "computer", "server", "equipment"]
                        },
                        "services": {
                            "name": "IT Services",
                            "keywords": ["IT service", "consulting", "support", "managed service", "outsourcing"]
                        },
                        "internet": {
                            "name": "Internet and Digital Media",
                            "keywords": ["internet", "web", "digital media", "online", "platform", "social media"]
                        }
                    }
                },
                "education": {
                    "name": "Education",
                    "description": "Organizations that provide educational services and resources.",
                    "keywords": [
                        "education", "school", "university", "college", "academic", "learning", 
                        "teaching", "student", "course", "training", "educational"
                    ],
                    "sub_industries": {
                        "k12": {
                            "name": "K-12 Education",
                            "keywords": ["school", "K-12", "elementary", "secondary", "high school"]
                        },
                        "higher_ed": {
                            "name": "Higher Education",
                            "keywords": ["university", "college", "higher education", "campus", "degree"]
                        },
                        "edtech": {
                            "name": "Educational Technology",
                            "keywords": ["edtech", "e-learning", "online learning", "educational software"]
                        },
                        "training": {
                            "name": "Professional Training",
                            "keywords": ["training", "professional development", "certification", "skill"]
                        }
                    }
                },
                "hospitality": {
                    "name": "Hospitality and Tourism",
                    "description": "Businesses that provide accommodation, food, and travel services.",
                    "keywords": [
                        "hospitality", "hotel", "restaurant", "tourism", "travel", "accommodation", 
                        "lodging", "food service", "catering", "leisure", "guest"
                    ],
                    "sub_industries": {
                        "accommodation": {
                            "name": "Accommodation",
                            "keywords": ["hotel", "motel", "resort", "lodging", "inn", "accommodation"]
                        },
                        "food_service": {
                            "name": "Food Service",
                            "keywords": ["restaurant", "cafe", "catering", "food service", "dining"]
                        },
                        "travel": {
                            "name": "Travel and Tourism",
                            "keywords": ["travel", "tourism", "tour", "vacation", "destination"]
                        },
                        "entertainment": {
                            "name": "Entertainment and Recreation",
                            "keywords": ["entertainment", "recreation", "attraction", "event", "leisure"]
                        }
                    }
                },
                "professional_services": {
                    "name": "Professional Services",
                    "description": "Businesses that provide specialized professional services.",
                    "keywords": [
                        "professional services", "consulting", "legal", "accounting", "advisory", 
                        "service firm", "professional", "expert", "consultant", "advisor"
                    ],
                    "sub_industries": {
                        "legal": {
                            "name": "Legal Services",
                            "keywords": ["legal", "law firm", "attorney", "lawyer", "counsel"]
                        },
                        "accounting": {
                            "name": "Accounting and Tax",
                            "keywords": ["accounting", "accountant", "tax", "audit", "bookkeeping"]
                        },
                        "consulting": {
                            "name": "Management Consulting",
                            "keywords": ["consulting", "consultant", "advisory", "strategy", "management"]
                        },
                        "marketing": {
                            "name": "Marketing and Advertising",
                            "keywords": ["marketing", "advertising", "agency", "PR", "media", "branding"]
                        }
                    }
                }
            }
        }
        
        # Save the default industry data
        with open(self.industry_data_path, 'w') as f:
            json.dump(default_industry_data, f, indent=4)
            
        return default_industry_data
    
    def classify_industry(self, 
                         business_description: str,
                         additional_keywords: Optional[List[str]] = None) -> Dict:
        """
        Classify the business industry based on the provided description.
        
        Args:
            business_description: Description of the business
            additional_keywords: Optional list of additional keywords to consider
            
        Returns:
            Dict: Classification results with confidence scores
        """
        # Normalize description to lowercase
        description_lower = business_description.lower()
        
        # Combine with additional keywords if provided
        if additional_keywords:
            description_lower += " " + " ".join([kw.lower() for kw in additional_keywords])
        
        # Initialize scores for each industry
        industry_scores = {}
        sub_industry_scores = {}
        
        # Calculate scores based on keyword matches
        for industry_id, industry_info in self.industry_data["industries"].items():
            # Initialize industry score
            industry_scores[industry_id] = 0
            sub_industry_scores[industry_id] = {}
            
            # Check for industry keywords
            for keyword in industry_info["keywords"]:
                # Count occurrences of the keyword
                count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', description_lower))
                if count > 0:
                    # Add to score based on occurrence count
                    industry_scores[industry_id] += count
            
            # Check for sub-industry keywords
            for sub_id, sub_info in industry_info["sub_industries"].items():
                sub_industry_scores[industry_id][sub_id] = 0
                
                for keyword in sub_info["keywords"]:
                    # Count occurrences of the keyword
                    count = len(re.findall(r'\b' + re.escape(keyword) + r'\b', description_lower))
                    if count > 0:
                        # Add to sub-industry score based on occurrence count
                        sub_industry_scores[industry_id][sub_id] += count
                        # Also add to parent industry score
                        industry_scores[industry_id] += count * 0.5  # Half weight for sub-industry keywords
        
        # Determine the top industry
        if not any(industry_scores.values()):
            # No matches found, default to technology
            top_industry_id = "technology"
            top_industry_confidence = 0
        else:
            # Get the industry with the highest score
            top_industry_id = max(industry_scores, key=industry_scores.get)
            # Calculate confidence as a percentage of the total score
            total_score = sum(industry_scores.values())
            top_industry_confidence = (industry_scores[top_industry_id] / total_score) * 100 if total_score > 0 else 0
        
        # Determine the top sub-industry for the top industry
        top_sub_industry = self._get_top_sub_industry(top_industry_id, sub_industry_scores)
        
        # Compile results
        classification_results = {
            "primary_industry": {
                "id": top_industry_id,
                "name": self.industry_data["industries"][top_industry_id]["name"],
                "confidence": round(top_industry_confidence, 2)
            },
            "sub_industry": top_sub_industry,
            "all_matches": {
                industry_id: {
                    "name": self.industry_data["industries"][industry_id]["name"],
                    "score": score,
                    "sub_industries": {
                        sub_id: {
                            "name": self.industry_data["industries"][industry_id]["sub_industries"][sub_id]["name"],
                            "score": sub_score
                        }
                        for sub_id, sub_score in sub_industry_scores[industry_id].items()
                        if sub_score > 0
                    }
                }
                for industry_id, score in industry_scores.items()
                if score > 0
            }
        }
        
        return classification_results
    
    def _get_top_sub_industry(self, industry_id: str, sub_industry_scores: Dict) -> Dict:
        """
        Get the top sub-industry for a given industry.
        
        Args:
            industry_id: The industry ID
            sub_industry_scores: Dictionary of sub-industry scores
            
        Returns:
            Dict: Top sub-industry information
        """
        # Get sub-industry scores for the specified industry
        sub_scores = sub_industry_scores.get(industry_id, {})
        
        if not sub_scores or not any(sub_scores.values()):
            # No sub-industry matches, return empty result
            return {
                "id": "",
                "name": "",
                "confidence": 0
            }
        
        # Get the sub-industry with the highest score
        top_sub_id = max(sub_scores, key=sub_scores.get)
        
        # Calculate confidence as a percentage of the total sub-industry score
        total_sub_score = sum(sub_scores.values())
        top_sub_confidence = (sub_scores[top_sub_id] / total_sub_score) * 100 if total_sub_score > 0 else 0
        
        return {
            "id": top_sub_id,
            "name": self.industry_data["industries"][industry_id]["sub_industries"][top_sub_id]["name"],
            "confidence": round(top_sub_confidence, 2)
        }
    
    def get_industry_information(self, industry_id: str) -> Dict:
        """
        Get detailed information about a specific industry.
        
        Args:
            industry_id: The industry ID
            
        Returns:
            Dict: Detailed industry information
        """
        if industry_id in self.industry_data["industries"]:
            return self.industry_data["industries"][industry_id]
        else:
            # Default to technology if industry not found
            return self.industry_data["industries"]["technology"]
    
    def update_industry_data(self, new_data: Dict) -> None:
        """
        Update the industry data with new information.
        
        Args:
            new_data: New industry data to add
        """
        # Merge new data with existing industry data
        if "industries" in new_data:
            for industry_id, industry_info in new_data["industries"].items():
                if industry_id in self.industry_data["industries"]:
                    # Update existing industry
                    for key, value in industry_info.items():
                        if key == "sub_industries" and "sub_industries" in self.industry_data["industries"][industry_id]:
                            # Merge sub-industries
                            for sub_id, sub_info in value.items():
                                if sub_id in self.industry_data["industries"][industry_id]["sub_industries"]:
                                    # Update existing sub-industry
                                    self.industry_data["industries"][industry_id]["sub_industries"][sub_id].update(sub_info)
                                else:
                                    # Add new sub-industry
                                    self.industry_data["industries"][industry_id]["sub_industries"][sub_id] = sub_info
                        elif key == "keywords" and "keywords" in self.industry_data["industries"][industry_id]:
                            # Merge keywords
                            self.industry_data["industries"][industry_id]["keywords"].extend(
                                [kw for kw in value if kw not in self.industry_data["industries"][industry_id]["keywords"]]
                            )
                        else:
                            # Update other fields
                            self.industry_data["industries"][industry_id][key] = value
                else:
                    # Add new industry
                    self.industry_data["industries"][industry_id] = industry_info
        
        # Save updated industry data
        with open(self.industry_data_path, 'w') as f:
            json.dump(self.industry_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    classifier = IndustryClassifier()
    
    # Classify a business description
    classification = classifier.classify_industry(
        business_description="We are an online retailer specializing in electronics and computer accessories.",
        additional_keywords=["e-commerce", "online store", "gadgets"]
    )
    
    print("Industry Classification:")
    print(f"Primary Industry: {classification['primary_industry']['name']} "
          f"(Confidence: {classification['primary_industry']['confidence']}%)")
    
    if classification['sub_industry']['id']:
        print(f"Sub-Industry: {classification['sub_industry']['name']} "
              f"(Confidence: {classification['sub_industry']['confidence']}%)")
    
    print("\nAll Matches:")
    for industry_id, info in classification['all_matches'].items():
        print(f"- {info['name']} (Score: {info['score']})")
        for sub_id, sub_info in info['sub_industries'].items():
            print(f"  - {sub_info['name']} (Score: {sub_info['score']})")
