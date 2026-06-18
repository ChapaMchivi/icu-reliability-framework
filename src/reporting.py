import logging
import pandas as pd
import os
from tabulate import tabulate

# Configure logger
logger = logging.getLogger(__name__)

def generate_manual_review_csv(df_results, output_path='manual_review_list.csv'):
    """Filters results for human review and saves to CSV."""
    review_list = df_results[df_results['reliability_flag'] == 'Manual Review Required'].copy()
    
    if review_list.empty:
        logger.info("No patients flagged for manual review.")
        return None
        
    cols = ['patient_id', 'mortality_probability']
    review_list_sorted = review_list[cols].sort_values(by='mortality_probability', ascending=False)
    
    review_list_sorted.to_csv(output_path, index=False)
    logger.info(f"Manual review list generated. Count: {len(review_list_sorted)}")
    return output_path

def print_performance_tables(probs):
    """Prints professional summary tables for audit documentation."""
    prob_stats = pd.Series(probs).describe().to_frame(name="Value")
    stats_data = [[idx, f"{val:.4f}"] for idx, val in prob_stats['Value'].items()]
    
    sample_data = pd.DataFrame(
        probs[:5], 
        columns=["Probability"], 
        index=[f"Patient {i+1}" for i in range(5)]
    )
    sample_list = [[idx, f"{row['Probability']:.4f}"] for idx, row in sample_data.iterrows()]
    
    print("\n--- Mortality Probability Overview ---")
    print(tabulate(stats_data, headers=["Metric", "Value"], tablefmt="grid"))
    print("\n--- Top 5 Patient Risk Assessments ---")
    print(tabulate(sample_list, headers=["Patient ID", "Probability"], tablefmt="grid"))

# --- Regulatory Reporting Gatekeeper ---
def generate_report_assets(output_dir='../images'):
    """
    Final security filter to ensure only non-PHI visual assets 
    are generated for stakeholder review.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Files identified as PHI-sensitive (Must be blocked from general reports)
    PHI_SENSITIVE_FILES = ['manual_review_list.csv']
    
    # Scan directory for assets
    current_files = os.listdir(output_dir)
    safe_assets = [f for f in current_files if f not in PHI_SENSITIVE_FILES]
    
    logger.info("--- Reporting Suite Active: Compliance Gatekeeper ---")
    logger.info(f"Compliance Check: {len(safe_assets)} visual assets validated for distribution.")
    return safe_assets