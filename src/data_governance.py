import pandas as pd
import logging
import hashlib
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# List of vital features required for ICU mortality prediction
REQUIRED_FEATURES = ['heart_rate_mean', 'systolic_bp_mean', 'glucose_mean', 'age', 'gender']

def load_and_validate_data(asset_name: str, asset_version: str):
    try:
        logger.info("Connecting to Azure ML Workspace...")
        ml_client = MLClient.from_config(credential=DefaultAzureCredential())
        
        data_asset = ml_client.data.get(name=asset_name, version=asset_version)
        df = pd.read_csv(data_asset.path)
        
        # Reliability Check: Ensure mandatory clinical features exist
        missing = [f for f in REQUIRED_FEATURES if f not in df.columns]
        if missing:
            raise ValueError(f"CRITICAL: Dataset is missing mandatory clinical features: {missing}")
            
        logger.info(f"Successfully validated data: {df.shape[0]} records loaded.")
        return df
    
    except Exception as e:
        logger.error(f"Data ingestion failed: {e}")
        raise

# --- HIPAA Compliance Utilities ---

def check_for_phi(df):
    """Scans the DataFrame for potential PHI columns."""
    phi_indicators = ['name', 'phone', 'address', 'zip', 'ssn', 'birth', 'email']
    found_phi = [col for col in df.columns if any(marker in col.lower() for marker in phi_indicators)]
    
    if found_phi:
        logger.error(f"HIPAA SECURITY ALERT: Potential PHI detected: {found_phi}")
        return False
    logger.info("Data pre-flight check passed: No PHI markers detected.")
    return True

def generate_surrogate_id(raw_id, salt="secure_random_salt_value"):
    """Creates a one-way hash (pseudonym) for a patient."""
    return hashlib.sha256((str(raw_id) + salt).encode()).hexdigest()[:12]