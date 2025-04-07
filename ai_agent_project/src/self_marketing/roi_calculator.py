"""
ROI Calculator Module

This module calculates and communicates the potential return on investment
for implementing the AI agent in different business contexts.
"""

import json
from typing import Dict, List, Optional, Tuple

class ROICalculator:
    """
    Calculates potential ROI for implementing the AI agent based on business context.
    """
    
    def __init__(self, metrics_data_path: str = "roi_metrics.json"):
        """
        Initialize the ROI Calculator.
        
        Args:
            metrics_data_path: Path to the metrics data file containing industry-specific ROI metrics
        """
        self.metrics_data_path = metrics_data_path
        self.metrics_data = self._load_metrics_data()
        
    def _load_metrics_data(self) -> Dict:
        """
        Load the metrics data from file.
        
        Returns:
            Dict: The metrics data
        """
        try:
            with open(self.metrics_data_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            # Return default metrics data if file not found or invalid
            return self._create_default_metrics_data()
    
    def _create_default_metrics_data(self) -> Dict:
        """
        Create default metrics data with industry-specific ROI information.
        
        Returns:
            Dict: Default metrics data
        """
        default_metrics = {
            "industries": {
                "retail": {
                    "time_savings": {
                        "min_percent": 15,
                        "max_percent": 30,
                        "description": "Reduction in time spent on customer service, inventory management, and sales forecasting"
                    },
                    "cost_reduction": {
                        "min_percent": 10,
                        "max_percent": 25,
                        "description": "Reduction in operational costs through automation and optimization"
                    },
                    "revenue_increase": {
                        "min_percent": 5,
                        "max_percent": 20,
                        "description": "Increase in revenue through improved customer engagement and sales optimization"
                    }
                },
                "healthcare": {
                    "time_savings": {
                        "min_percent": 20,
                        "max_percent": 35,
                        "description": "Reduction in administrative time for patient scheduling and record management"
                    },
                    "cost_reduction": {
                        "min_percent": 12,
                        "max_percent": 28,
                        "description": "Reduction in operational costs through streamlined processes"
                    },
                    "revenue_increase": {
                        "min_percent": 3,
                        "max_percent": 15,
                        "description": "Increase in revenue through improved patient throughput and service quality"
                    }
                },
                "finance": {
                    "time_savings": {
                        "min_percent": 18,
                        "max_percent": 32,
                        "description": "Reduction in time spent on risk assessment, fraud detection, and customer service"
                    },
                    "cost_reduction": {
                        "min_percent": 15,
                        "max_percent": 30,
                        "description": "Reduction in operational costs through automated risk assessment and fraud detection"
                    },
                    "revenue_increase": {
                        "min_percent": 4,
                        "max_percent": 18,
                        "description": "Increase in revenue through improved customer service and risk management"
                    }
                },
                "manufacturing": {
                    "time_savings": {
                        "min_percent": 15,
                        "max_percent": 30,
                        "description": "Reduction in time spent on production planning, quality control, and supply chain management"
                    },
                    "cost_reduction": {
                        "min_percent": 12,
                        "max_percent": 25,
                        "description": "Reduction in operational costs through optimized production and supply chain"
                    },
                    "revenue_increase": {
                        "min_percent": 5,
                        "max_percent": 15,
                        "description": "Increase in revenue through improved product quality and production efficiency"
                    }
                },
                "technology": {
                    "time_savings": {
                        "min_percent": 20,
                        "max_percent": 40,
                        "description": "Reduction in time spent on development, customer support, and product innovation"
                    },
                    "cost_reduction": {
                        "min_percent": 15,
                        "max_percent": 30,
                        "description": "Reduction in operational costs through automated development and support processes"
                    },
                    "revenue_increase": {
                        "min_percent": 8,
                        "max_percent": 25,
                        "description": "Increase in revenue through improved product innovation and customer satisfaction"
                    }
                }
            },
            "business_sizes": {
                "small": {
                    "implementation_cost_factor": 0.7,
                    "time_to_roi_months": {"min": 3, "max": 6}
                },
                "medium": {
                    "implementation_cost_factor": 1.0,
                    "time_to_roi_months": {"min": 4, "max": 8}
                },
                "enterprise": {
                    "implementation_cost_factor": 1.5,
                    "time_to_roi_months": {"min": 6, "max": 12}
                }
            },
            "base_implementation_cost": {
                "currency": "USD",
                "amount": 10000
            },
            "annual_subscription": {
                "currency": "USD",
                "amount": 5000
            }
        }
        
        # Save the default metrics data
        with open(self.metrics_data_path, 'w') as f:
            json.dump(default_metrics, f, indent=4)
            
        return default_metrics
    
    def calculate_roi(self, 
                     industry: str, 
                     business_size: str,
                     annual_revenue: float,
                     employees_count: int,
                     current_costs: Optional[Dict[str, float]] = None) -> Dict:
        """
        Calculate ROI based on business context and financial information.
        
        Args:
            industry: The industry of the business
            business_size: The size of the business (small, medium, enterprise)
            annual_revenue: Annual revenue of the business
            employees_count: Number of employees in the business
            current_costs: Optional dictionary with current operational costs
            
        Returns:
            Dict: ROI calculation results
        """
        # Normalize inputs to lowercase
        industry = industry.lower()
        business_size = business_size.lower()
        
        # Get industry data or default to technology if not found
        industry_data = self.metrics_data["industries"].get(
            industry, self.metrics_data["industries"]["technology"]
        )
        
        # Get business size data or default to medium if not found
        size_data = self.metrics_data["business_sizes"].get(
            business_size, self.metrics_data["business_sizes"]["medium"]
        )
        
        # Calculate implementation cost
        base_cost = self.metrics_data["base_implementation_cost"]["amount"]
        implementation_cost = base_cost * size_data["implementation_cost_factor"]
        
        # Calculate annual subscription cost
        annual_subscription = self.metrics_data["annual_subscription"]["amount"]
        
        # Calculate total first year cost
        total_first_year_cost = implementation_cost + annual_subscription
        
        # Calculate potential savings and revenue increases
        time_savings_min = industry_data["time_savings"]["min_percent"] / 100
        time_savings_max = industry_data["time_savings"]["max_percent"] / 100
        
        cost_reduction_min = industry_data["cost_reduction"]["min_percent"] / 100
        cost_reduction_max = industry_data["cost_reduction"]["max_percent"] / 100
        
        revenue_increase_min = industry_data["revenue_increase"]["min_percent"] / 100
        revenue_increase_max = industry_data["revenue_increase"]["max_percent"] / 100
        
        # Estimate operational costs if not provided
        if current_costs is None:
            # Rough estimate: operational costs are typically 70-80% of revenue for most businesses
            estimated_operational_costs = annual_revenue * 0.75
            labor_costs = estimated_operational_costs * 0.4  # Labor typically 30-50% of operational costs
            other_costs = estimated_operational_costs * 0.6
        else:
            labor_costs = current_costs.get("labor", annual_revenue * 0.3)
            other_costs = current_costs.get("other", annual_revenue * 0.45)
        
        # Calculate potential savings
        labor_savings_min = labor_costs * time_savings_min
        labor_savings_max = labor_costs * time_savings_max
        
        other_savings_min = other_costs * cost_reduction_min
        other_savings_max = other_costs * cost_reduction_max
        
        # Calculate potential revenue increase
        revenue_increase_amount_min = annual_revenue * revenue_increase_min
        revenue_increase_amount_max = annual_revenue * revenue_increase_max
        
        # Calculate total annual benefit
        total_benefit_min = labor_savings_min + other_savings_min + revenue_increase_amount_min
        total_benefit_max = labor_savings_max + other_savings_max + revenue_increase_amount_max
        
        # Calculate first year ROI
        first_year_roi_min = (total_benefit_min - total_first_year_cost) / total_first_year_cost * 100
        first_year_roi_max = (total_benefit_max - total_first_year_cost) / total_first_year_cost * 100
        
        # Calculate subsequent years ROI (without implementation cost)
        subsequent_roi_min = (total_benefit_min - annual_subscription) / annual_subscription * 100
        subsequent_roi_max = (total_benefit_max - annual_subscription) / annual_subscription * 100
        
        # Calculate payback period in months
        if total_benefit_min > 0:
            payback_months_max = (total_first_year_cost / (total_benefit_min / 12))
        else:
            payback_months_max = 24  # Default to 24 months if benefit is zero or negative
            
        if total_benefit_max > 0:
            payback_months_min = (total_first_year_cost / (total_benefit_max / 12))
        else:
            payback_months_min = 12  # Default to 12 months if benefit is zero or negative
        
        # Compile results
        roi_results = {
            "implementation_cost": round(implementation_cost, 2),
            "annual_subscription": round(annual_subscription, 2),
            "total_first_year_cost": round(total_first_year_cost, 2),
            "annual_benefits": {
                "labor_savings": {
                    "min": round(labor_savings_min, 2),
                    "max": round(labor_savings_max, 2),
                    "description": industry_data["time_savings"]["description"]
                },
                "operational_savings": {
                    "min": round(other_savings_min, 2),
                    "max": round(other_savings_max, 2),
                    "description": industry_data["cost_reduction"]["description"]
                },
                "revenue_increase": {
                    "min": round(revenue_increase_amount_min, 2),
                    "max": round(revenue_increase_amount_max, 2),
                    "description": industry_data["revenue_increase"]["description"]
                },
                "total_benefit": {
                    "min": round(total_benefit_min, 2),
                    "max": round(total_benefit_max, 2)
                }
            },
            "roi": {
                "first_year": {
                    "min": round(first_year_roi_min, 2),
                    "max": round(first_year_roi_max, 2)
                },
                "subsequent_years": {
                    "min": round(subsequent_roi_min, 2),
                    "max": round(subsequent_roi_max, 2)
                }
            },
            "payback_period_months": {
                "min": round(payback_months_min, 1),
                "max": round(payback_months_max, 1)
            },
            "currency": self.metrics_data["base_implementation_cost"]["currency"]
        }
        
        return roi_results
    
    def generate_roi_summary(self, roi_data: Dict) -> str:
        """
        Generate a human-readable summary of the ROI calculation.
        
        Args:
            roi_data: ROI calculation results from calculate_roi method
            
        Returns:
            str: A formatted ROI summary
        """
        currency = roi_data["currency"]
        
        summary = f"ROI Summary\n"
        summary += f"===========\n\n"
        
        summary += f"Investment:\n"
        summary += f"- Implementation Cost: {currency} {roi_data['implementation_cost']:,.2f}\n"
        summary += f"- Annual Subscription: {currency} {roi_data['annual_subscription']:,.2f}\n"
        summary += f"- Total First Year Cost: {currency} {roi_data['total_first_year_cost']:,.2f}\n\n"
        
        summary += f"Annual Benefits:\n"
        
        labor = roi_data["annual_benefits"]["labor_savings"]
        summary += f"- Labor Savings: {currency} {labor['min']:,.2f} to {currency} {labor['max']:,.2f}\n"
        summary += f"  ({labor['description']})\n\n"
        
        ops = roi_data["annual_benefits"]["operational_savings"]
        summary += f"- Operational Savings: {currency} {ops['min']:,.2f} to {currency} {ops['max']:,.2f}\n"
        summary += f"  ({ops['description']})\n\n"
        
        rev = roi_data["annual_benefits"]["revenue_increase"]
        summary += f"- Revenue Increase: {currency} {rev['min']:,.2f} to {currency} {rev['max']:,.2f}\n"
        summary += f"  ({rev['description']})\n\n"
        
        total = roi_data["annual_benefits"]["total_benefit"]
        summary += f"- Total Annual Benefit: {currency} {total['min']:,.2f} to {currency} {total['max']:,.2f}\n\n"
        
        summary += f"Return on Investment:\n"
        first_year = roi_data["roi"]["first_year"]
        summary += f"- First Year ROI: {first_year['min']}% to {first_year['max']}%\n"
        
        subsequent = roi_data["roi"]["subsequent_years"]
        summary += f"- Subsequent Years ROI: {subsequent['min']}% to {subsequent['max']}%\n\n"
        
        payback = roi_data["payback_period_months"]
        summary += f"Payback Period: {payback['min']} to {payback['max']} months\n"
        
        return summary
    
    def update_metrics_data(self, new_data: Dict) -> None:
        """
        Update the metrics data with new information.
        
        Args:
            new_data: New metrics data to add
        """
        # Merge new data with existing metrics data
        for category, category_data in new_data.items():
            if category in self.metrics_data:
                for key, value in category_data.items():
                    if key in self.metrics_data[category]:
                        # Update existing entry
                        if isinstance(value, dict) and isinstance(self.metrics_data[category][key], dict):
                            self.metrics_data[category][key].update(value)
                        else:
                            self.metrics_data[category][key] = value
                    else:
                        # Add new entry
                        self.metrics_data[category][key] = value
            else:
                # Add new category
                self.metrics_data[category] = category_data
                
        # Save updated metrics data
        with open(self.metrics_data_path, 'w') as f:
            json.dump(self.metrics_data, f, indent=4)


# Example usage
if __name__ == "__main__":
    calculator = ROICalculator()
    
    # Calculate ROI for a retail business
    roi_data = calculator.calculate_roi(
        industry="retail",
        business_size="medium",
        annual_revenue=5000000,
        employees_count=50
    )
    
    # Generate and print ROI summary
    summary = calculator.generate_roi_summary(roi_data)
    print(summary)
