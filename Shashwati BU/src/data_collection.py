import os
import pandas as pd
from src.config import RAW_DATA_DIR

def load_dataset(file_path: str):
    """Load dataset into pandas DataFrame."""
    return pd.read_csv(file_path)

if __name__ == "__main__":
    os.makedirs(RAW_DATA_DIR, exist_ok=True)
    dataset_path = os.path.join(RAW_DATA_DIR, "heart.csv")

    # Example: if dataset already downloaded manually
    if os.path.exists(dataset_path):
        df = load_dataset(dataset_path)
        print("✅ Data loaded successfully!")
        print("Shape:", df.shape)
    else:
        print("⚠️ Please download and place heart.csv in data/raw/")
