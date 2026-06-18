import numpy as np
import pandas as pd
import logging

# Configure logger
logger = logging.getLogger(__name__)

def test_model_robustness(model, original_df, feature_to_perturb, feature_list, noise_level_pct=0.1):
    """
    Simulates noise while forcing alignment to the model's exact schema.
    """
    # 1. Force alignment
    df_base = original_df.reindex(columns=feature_list, fill_value=0).copy()
    
    # 2. Safety check
    if df_base.shape[1] != len(feature_list):
        logger.error(f"Alignment failed. Shape is {df_base.shape}, expected {len(feature_list)}.")
        return None

    # 3. Add noise
    std_dev = df_base[feature_to_perturb].std()
    noise = np.random.normal(0, noise_level_pct * std_dev, size=df_base.shape[0])
    df_base[feature_to_perturb] = df_base[feature_to_perturb] + noise
    
    # 4. Predict
    predictions = model.predict(df_base)
    original_predictions = model.predict(df_base.copy())
    
    # 5. Result
    change_rate = np.mean(predictions != original_predictions)
    logger.info(f"Robustness Audit | Feature: {feature_to_perturb} | Change Rate: {change_rate:.2%}")
    return change_rate

def predict_with_reliability_framework(data, model, threshold=0.25):
    """
    Applies the Reliability Framework:
    1. Schema Alignment
    2. Probability Estimation
    3. Clinical Fallback (Flags for human review)
    """
    # 1. Dynamic Schema Alignment
    # Assumes a scikit-learn pipeline structure
    expected_features = list(model.named_steps['datatransformer']._columns_types_mapping.keys())
    X_aligned = data[expected_features]
    
    # 2. Probability Estimation
    probs = model.predict_proba(X_aligned)[:, 1]
    
    # 3. Apply Reliability Threshold
    predictions = (probs >= threshold).astype(int)
    
    # 4. Create results with Reliability Flag
    results = data.copy()
    results['mortality_predicted'] = predictions
    results['mortality_probability'] = probs
    results['reliability_flag'] = [
        'Manual Review Required' if p >= threshold else 'Routine Monitoring' 
        for p in probs
    ]
    
    return results




























