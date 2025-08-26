import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.config import PROCESSED_DATA_DIR
import os

def run_eda():
    dataset_path = os.path.join(PROCESSED_DATA_DIR, "heart_clean.csv")
    df = pd.read_csv(dataset_path)

    print("Dataset shape:", df.shape)
    print("\nData types:\n", df.dtypes)
    print("\nSummary statistics:\n", df.describe())

    # Missing values
    print("\nMissing values:\n", df.isnull().sum())

    # Visualizations
    sns.histplot(df['age'])
    plt.title("Age Distribution")
    plt.show()

    corr = df.corr(numeric_only=True)  # ✅ Only numeric columns
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()

if __name__ == "__main__":
    run_eda()
