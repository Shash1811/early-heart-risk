import pandas as pd
import numpy as np
from src.config import HEART_DATASET, PROCESSED_DATA_DIR
import os

def clean_data():
    df = pd.read_csv(HEART_DATASET)

    # Replace '?' with NaN
    df.replace("?", np.nan, inplace=True)

    # Convert numeric columns to proper types
    df["ca"] = pd.to_numeric(df["ca"], errors="coerce")
    df["thal"] = pd.to_numeric(df["thal"], errors="coerce")
    df["num"] = pd.to_numeric(df["num"], errors="coerce")

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values (simple imputation: median for numeric, mode for categorical)
    for col in df.columns:
        if df[col].dtype in ["float64", "int64"]:
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna(df[col].mode()[0], inplace=True)

    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    save_path = os.path.join(PROCESSED_DATA_DIR, "heart_clean.csv")
    df.to_csv(save_path, index=False)
    print(f"✅ Clean dataset saved to {save_path}")

if __name__ == "__main__":
    clean_data()
