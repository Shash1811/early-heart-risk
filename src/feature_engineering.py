import pandas as pd
from src.config import PROCESSED_DATA_DIR
import os

def engineer_features():
    df = pd.read_csv(os.path.join(PROCESSED_DATA_DIR, "heart_clean.csv"))

    # Example: Create BMI category if height/weight existed
    # df["BMI"] = df["weight"] / (df["height"]/100)**2

    # Example: Age groups
    df["age_group"] = pd.cut(df["age"], bins=[20, 40, 60, 80], labels=["Young", "Middle", "Senior"])

    save_path = os.path.join(PROCESSED_DATA_DIR, "heart_features.csv")
    df.to_csv(save_path, index=False)
    print(f"✅ Feature engineered dataset saved to {save_path}")

if __name__ == "__main__":
    engineer_features()
