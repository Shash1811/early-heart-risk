import os

# Base project directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Data paths
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

# Example dataset name (replace with actual)
HEART_DATASET = os.path.join(RAW_DATA_DIR, "heart.csv")
