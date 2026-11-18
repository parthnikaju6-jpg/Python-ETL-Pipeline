
import pandas as pd


def transform_data(df):

    print("Starting data transformation...")

    # 1. Remove duplicate records
    df = df.drop_duplicates()

    # 2. Remove rows with missing customer names
    df = df.dropna(subset=["CustomerName"])

    # 3. Remove records where quantity is zero or negative
    df = df[df["Quantity"] > 0]

    # 4. Convert OrderDate into datetime format
    df["OrderDate"] = pd.to_datetime(df["OrderDate"])

    # 5. Create TotalAmount column
    df["TotalAmount"] = df["Quantity"] * df["UnitPrice"]

    print("\nData cleaning completed!")

    print("\nCleaned Data:")
    print(df)

    print("\nCleaned Dataset Shape:")
    print(df.shape)

    print("\nMissing Values:")
    print(df.isnull().sum())

    return df
