
from pathlib import Path
import sqlite3
import pandas as pd

# Database location
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_FILE = PROJECT_ROOT / "sales.db"


def load_data(df):

    # Connect to SQLite database
    connection = sqlite3.connect(DB_FILE)

    try:
        # Load DataFrame into database table
        df.to_sql(
            name="sales",
            con=connection,
            if_exists="replace",
            index=False
        )

        print("Data loaded successfully!")

        # Check number of records loaded
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM sales")

        count = cursor.fetchone()[0]

        print("Total records loaded:", count)

        cursor.execute("SELECT * FROM sales LIMIT 5")

        rows = cursor.fetchall()

        print("\nFirst 5 records from database:")
        for row in rows:
            print(row)

    finally:
        connection.close()


if __name__ == "__main__":
    print("Run main.py to execute the complete ETL pipeline.")
