from src.data_cleaning import clean_data
from src.feature_engineering import engineer_features
from src.eda import run_eda

def run_pipeline():
    print("▶ Running Data Cleaning...")
    clean_data()

    print("▶ Running Feature Engineering...")
    engineer_features()

    print("▶ Running EDA...")
    run_eda()

    print("✅ Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
