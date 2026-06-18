import os
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report

def plot_confusion_matrix(y_true, y_pred, title, cmap='Blues', save_path=None):
    """Generates and optionally saves a confusion matrix heatmap."""
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap=cmap, 
                xticklabels=['Predicted Alive', 'Predicted Mortality'],
                yticklabels=['Actual Alive', 'Actual Mortality'])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title(title)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close() # Essential for memory management in batch environments

def plot_classification_report(y_true, y_pred, save_path=None):
    """Visualizes the classification report as a heatmap."""
    report = classification_report(y_true, y_pred, output_dict=True)
    df_report = pd.DataFrame(report).transpose()
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(df_report, annot=True, cmap='Blues', fmt='.2f', cbar=False)
    plt.title('Classification Report: Model Performance')
    plt.yticks(rotation=0)
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close() # Essential for memory management in batch environments

def plot_fairness_table(df_fairness, save_path=None):
    """Renders a fairness metric dataframe as an image table."""
    fig, ax = plt.subplots(figsize=(8, 2))
    ax.axis('off')
    table = ax.table(cellText=df_fairness.values, colLabels=df_fairness.columns, 
                     loc='center', cellLoc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1.2, 1.5)
    plt.title("Fairness Assessment: Performance by Gender")
    
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
    plt.show()
    plt.close() # Essential for memory management in batch environments



















