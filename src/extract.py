
from pathlib import Path
import pandas as pd

# Get the main project folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]

# Location of the raw CSV file
RAW_FILE = PROJECT_ROOT / "data" / "raw_sales.csv"


def extract_data():
    # Read CSV file using Pandas
    df = pd.read_csv(RAW_FILE)

    print("Data extracted successfully!")

    # Display first 5 records
    print("\nFirst 5 Records:")
    print(df.head())

    # Display number of rows and columns
    print("\nDataset Shape:")
    print(df.shape)

    # Display column information
    print("\nDataset Information:")
    df.info()

    return df


if __name__ == "__main__":
    extract_data()
