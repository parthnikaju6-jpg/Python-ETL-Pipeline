
from src.extract import extract_data
from src.transform import transform_data
from src.load import load_data

# Step 1: Extract
raw_df = extract_data()

# Step 2: Transform
cleaned_df = transform_data(raw_df)

# Step 3: Load
load_data(cleaned_df)

print("\nETL Pipeline completed successfully!")
