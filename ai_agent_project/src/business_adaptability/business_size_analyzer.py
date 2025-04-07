"""
Business Size Analyzer Module

This module determines the scale and complexity of a business based on provided information.
"""

import json
from typing import Dict, List, Optional, Tuple

class BusinessSizeAnalyzer:
    """
    Analyzes and determines the business size category.
    """
    
    def __init__(self, size_data_path: str = "business_size_data.json"):
        """
        Initialize the Business Size Analyzer.
        
        Args:
            size_data_path: Path to the business size data file
        """
        self.size_data_path = size_data_path
        self.size_data = self._load_size_data()
        
    def _load_size_data(self) -> Dict:
        """
        Load the business size data from file.
        
        Returns:
            Dict: The business size data
        """
        try:
            with open(self.size_data_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default size data if file not found or invalid
            return self._create_default_size_data()
    
    def _create_default_size_data(self) -> Dict:
        """
        Create default business size data with classifications and thresholds.
        
        Returns:
            Dict: Default business size data
        """
        default_size_data = {
            "general_thresholds": {
                "employees": {
                    "micro": {"min": 1, "max": 10},
                    "small": {"min": 11, "max": 50},
                    "medium": {"min": 51, "max": 250},
                    "large": {"min": 251, "max": 1000},
                    "enterprise": {"min": 1001, "max": None}
                },
                "revenue": {  # Annual revenue in USD
                    "micro": {"min": 0, "max": 1000000},
                    "small": {"min": 1000001, "max": 10000000},
                    "medium": {"min": 10000001, "max": 50000000},
                    "large": {"min": 50000001, "max": 1000000000},
                    "enterprise": {"min": 1000000001, "max": None}
                }
            },
            "industry_specific_thresholds": {
                "retail": {
                    "employees": {
                        "small": {"min": 1, "max": 50},
                        "medium": {"min": 51, "max": 200},
                        "enterprise": {"min": 201, "max": None}
                    },
                    "revenue": {
                        "small": {"min": 0, "max": 5000000},
                        "medium": {"min": 5000001, "max": 50000000},
                        "enterprise": {"min": 50000001, "max": None}
                    },
                    "locations": {
                        "small": {"min": 1, "max": 3},
                        "medium": {"min": 4, "max": 20},
                        "enterprise": {"min": 21, "max": None}
                    }
                },
                "healthcare": {
                    "employees": {
                        "small": {"min": 1, "max": 100},
                        "medium": {"min": 101, "max": 500},
                        "enterprise": {"min": 501, "max": None}
                    },
                    "revenue": {
                        "small": {"min": 0, "max": 10000000},
                        "medium": {"min": 10000001, "max": 100000000},
                        "enterprise": {"min": 100000001, "max": None}
                    },
                    "beds": {  # For hospitals
                        "small": {"min": 1, "max": 100},
                        "medium": {"min": 101, "max": 500},
                        "enterprise": {"min": 501, "max": None}
                    }
                },
                "finance": {
                    "employees": {
                        "small": {"min": 1, "max": 100},
                        "medium": {"min": 101, "max": 1000},
                        "enterprise": {"min": 1001, "max": None}
                    },
                    "revenue": {
                        "small": {"min": 0, "max": 20000000},
                        "medium": {"min": 20000001, "max": 500000000},
                        "enterprise": {"min": 500000001, "max": None}
                    },
                    "assets_under_management": {
                        "small": {"min": 0, "max": 100000000},
                        "medium": {"min": 100000001, "max": 1000000000},
                        "enterprise": {"min": 1000000001, "max": None}
                    }
                },
                "manufacturing": {
                    "employees": {
                        "small": {"min": 1, "max": 100},
                        "medium": {"min": 101, "max": 500},
                        "enterprise": {"min": 501, "max": None}
                    },
                    "revenue": {
                        "small": {"min": 0, "max": 20000000},
                        "medium": {"min": 20000001, "max": 100000000},
                        "enterprise": {"min": 100000001, "max": None}
                    },
                    "production_volume": {
                        "small": {"min": 0, "max": 1000000},
                        "medium": {"min": 1000001, "max": 10000000},
                        "enterprise": {"min": 10000001, "max": None}
                    }
                },
                "technology": {
                    "employees": {
                        "small": {"min": 1, "max": 50},
                        "medium": {"min": 51, "max": 250},
                        "enterprise": {"min": 251, "max": None}
                    },
                    "revenue": {
                        "small": {"min": 0, "max": 10000000},
                        "medium": {"min": 10000001, "max": 100000000},
                        "enterprise": {"min": 100000001, "max": None}
                    },
                    "users": {
                        "small": {"min": 0, "max": 10000},
                        "medium": {"min": 10001, "max": 1000000},
                        "enterprise": {"min": 1000001, "max": None}
                    }
                }
            },
            "size_characteristics": {
                "small": {
                    "description": "Small businesses typically have limited resources, simpler organizational structures, and more direct decision-making processes.",
                    "challenges": [
                        "Limited budget and resources",
                        "Wearing multiple hats (employees perform multiple roles)",
                        "Difficulty competing with larger businesses",
                        "Limited access to capital",
                        "Less formal processes and documentation"
                    ],
                    "opportunities": [
                        "Agility and quick decision-making",
                        "Personal customer relationships",
                        "Niche market focus",
                        "Flexibility to adapt quickly",
                        "Less bureaucracy"
                    ]
                },
                "medium": {
                    "description": "Medium-sized businesses have more resources than small businesses but still maintain some flexibility. They typically have more formal structures and specialized roles.",
                    "challenges": [
                        "Growing pains during scaling",
                        "Balancing formality with flexibility",
                        "Developing middle management",
                        "Standardizing processes across the organization",
                        "Competing with both small and large businesses"
                    ],
                    "opportunities": [
                        "Established market presence",
                        "More resources for growth and innovation",
                        "Ability to serve larger clients",
                        "More specialized expertise",
                        "Better economies of scale than small businesses"
                    ]
                },
                "enterprise": {
                    "description": "Enterprise businesses are large organizations with complex structures, formal processes, and significant resources. They typically operate at scale across multiple locations or markets.",
                    "challenges": [
                        "Organizational complexity",
                        "Slower decision-making processes",
                        "Maintaining innovation and agility",
                        "Managing large workforces",
                        "Coordinating across departments and regions"
                    ],
                    "opportunities": [
                        "Significant resources for investment",
                        "Strong market position and brand recognition",
                        "Economies of scale",
                        "Ability to influence industry standards",
                        "Global reach and capabilities"
                    ]
                }
            }
        }
        
        # Save the default size data
        with open(self.size_data_path, 'w') as f:
            json.dump(default_size_data, f, indent=4)
            
        return default_size_data
    
    def analyze_business_size(self, 
                             industry: str,
                             employees_count: Optional[int] = None,
                             annual_revenue: Optional[float] = None,
                             additional_metrics: Optional[Dict] = None) -> Dict:
        """
        Analyze and determine the business size category based on provided metrics.
        
        Args:
            industry: The industry of the business
            employees_count: Number of employees
            annual_revenue: Annual revenue in USD
            additional_metrics: Optional dictionary with additional industry-specific metrics
            
        Returns:
            Dict: Business size analysis results
        """
        # Normalize industry to lowercase
        industry = industry.lower()
        
        # Initialize results
        size_categories = []
        confidence_scores = {}
        
        # Get industry-specific thresholds if available, otherwise use general thresholds
        if industry in self.size_data["industry_specific_thresholds"]:
            thresholds = self.size_data["industry_specific_thresholds"][industry]
        else:
            # Default to general thresholds
            thresholds = {"employees": self.size_data["general_thresholds"]["employees"],
                         "revenue": self.size_data["general_thresholds"]["revenue"]}
        
        # Analyze employees count if provided
        if employees_count is not None and "employees" in thresholds:
            employee_size = self._categorize_metric(employees_count, thresholds["employees"])
            if employee_size:
                size_categories.append(employee_size)
                confidence_scores["employees"] = {"size": employee_size, "weight": 0.4}  # 40% weight
        
        # Analyze annual revenue if provided
        if annual_revenue is not None and "revenue" in thresholds:
            revenue_size = self._categorize_metric(annual_revenue, thresholds["revenue"])
            if revenue_size:
                size_categories.append(revenue_size)
                confidence_scores["revenue"] = {"size": revenue_size, "weight": 0.4}  # 40% weight
        
        # Analyze additional metrics if provided
        if additional_metrics:
            for metric_name, value in additional_metrics.items():
                if metric_name in thresholds:
                    metric_size = self._categorize_metric(value, thresholds[metric_name])
                    if metric_size:
                        size_categories.append(metric_size)
                        confidence_scores[metric_name] = {"size": metric_size, "weight": 0.2}  # 20% weight for additional metrics
        
        # Determine the final size category
        if not size_categories:
            # Default to medium if no metrics provided
            final_size = "medium"
            final_confidence = 0
        else:
            # Count occurrences of each size category
            size_counts = {}
            for size in size_categories:
                size_counts[size] = size_counts.get(size, 0) + 1
            
            # Get the most common size category
            final_size = max(size_counts, key=size_counts.get)
            
            # Calculate confidence score
            if len(confidence_scores) > 0:
                # Calculate weighted confidence
                weighted_confidence = 0
                total_weight = 0
                
                for metric, info in confidence_scores.items():
                    if info["size"] == final_size:
                        weighted_confidence += info["weight"]
                    total_weight += info["weight"]
                
                final_confidence = (weighted_confidence / total_weight) * 100 if total_weight > 0 else 0
            else:
                final_confidence = 0
        
        # Get size characteristics
        size_characteristics = self.size_data["size_characteristics"].get(
            final_size, self.size_data["size_characteristics"]["medium"]
        )
        
        # Compile results
        analysis_results = {
            "size_category": final_size,
            "confidence": round(final_confidence, 2),
            "description": size_characteristics["description"],
            "challenges": size_characteristics["challenges"],
            "opportunities": size_characteristics["opportunities"],
            "metrics_analysis": {
                metric: {
                    "value": value,
                    "category": info["size"],
                    "weight": info["weight"]
                }
                for metric, info in confidence_scores.items()
            }
        }
        
        return analysis_results
    
    def _categorize_metric(self, value: float, thresholds: Dict) -> str:
        """
        Categorize a metric value based on thresholds.
        
        Args:
            value: The metric value
            thresholds: Dictionary of thresholds for different size categories
            
        Returns:
            str: The size category for the metric value
        """
        for size, range_info in thresholds.items():
            min_val = range_info["min"]
            max_val = range_info["max"]
            
            if min_val is not None and max_val is not None:
                if min_val <= value <= max_val:
                    return size
            elif min_val is not None and max_val is None:
                if value >= min_val:
                    return size
            elif min_val is None and max_val is not None:
                if value <= max_val:
                    return size
        
        # Default to medium if no match found
        return "medium"
    
    def get_size_information(self, size_category: str) -> Dict:
        """
        Get detailed information about a specific business size category.
        
        Args:
            size_category: The business size category
            
        Returns:
            Dict: Detailed size information
        """
        # Normalize size category to lowercase
        size_category = size_category.lower()
        
        if size_category in self.size_data["size_characteristics"]:
            return self.size_data["size_characteristics"][size_category]
        else:
            # Default to medium if size category not found
            return self.size_data["size_characteristics"]["medium"]
    
    def update_size_data(self, new_data: Dict) -> None:
        """
        Update the business size data with new information.
        
        Args:
            new_data: New business size data to add
        """
        # Merge new data with existing size data
        for category, category_data in new_data.items():
            if category in self.size_data:
                if isinstance(category_data, dict):
                    for key, value in category_data.items():
                        if key in self.size_data[category]:
                            # Update existing entry
                            if isinstance(value, dict) and isinstance(self.size_data[category][key], dict):
                                self.size_data[category][key].update(value)
                            else:
                                self.size_data[category][key] = value
                        else:
                            # Add new entry
                            self.size_data[category][key] = value
                elif isinstance(category_data, list):
                    # For list types, append new items
                    self.size_data[category].extend(category_data)
            else:
                # Add new category
                self.size_data[category] = category_data
                
        # Save updated size data
        with open(self.size_data_path, 'w') as f:
            json.dump(self.size_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    analyzer = BusinessSizeAnalyzer()
    
    # Analyze a business
    analysis = analyzer.analyze_business_size(
        industry="retail",
        employees_count=75,
        annual_revenue=8000000,
        additional_metrics={"locations": 5}
    )
    
    print("Business Size Analysis:")
    print(f"Size Category: {analysis['size_category'].capitalize()}")
    print(f"Confidence: {analysis['confidence']}%")
    print(f"\nDescription: {analysis['description']}")
    
    print("\nChallenges:")
    for challenge in analysis['challenges']:
        print(f"- {challenge}")
    
    print("\nOpportunities:")
    for opportunity in analysis['opportunities']:
        print(f"- {opportunity}")
    
    print("\nMetrics Analysis:")
    for metric, info in analysis['metrics_analysis'].items():
        print(f"- {metric.capitalize()}: {info['value']} (Category: {info['category'].capitalize()}, Weight: {info['weight']})")
