# Quick script to generate predictions with confidence scores for testing BetBuilder
import pandas as pd
import numpy as np

# Create sample prediction data with confidence scores
sample_data = {
    'race_id': ['ASD_1', 'ASD_1', 'ASD_1', 'ASD_1', 'ASD_2', 'ASD_2', 'ASD_2', 'ASD_2', 'ASD_2'],
    'horse_id': ['Horse1_1', 'Horse2_2', 'Horse3_3', 'Horse4_4', 'Horse5_1', 'Horse6_2', 'Horse7_3', 'Horse8_4', 'Horse9_5'],
    'predicted_finish_position': [1.2, 2.1, 3.5, 4.8, 1.8, 2.3, 2.9, 3.7, 5.1],
    'confidence_score': [85.5, 72.3, 45.2, 35.8, 78.9, 68.4, 62.1, 48.5, 28.7]
}

# Create DataFrame
predictions_df = pd.DataFrame(sample_data)

# Save to CSV with current date format
filename = "predictions_asd_20250625.csv"
predictions_df.to_csv(filename, index=False)

print(f"Sample predictions saved to {filename}")
print("\nSample data:")
print(predictions_df)
print(f"\nConfidence score range: {predictions_df['confidence_score'].min():.1f} - {predictions_df['confidence_score'].max():.1f}")
print(f"Average confidence: {predictions_df['confidence_score'].mean():.1f}")
