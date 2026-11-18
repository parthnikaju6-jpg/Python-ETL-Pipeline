
from pathlib import Path
import sqlite3

# Locate the database
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DB_FILE = PROJECT_ROOT / "sales.db"

# Connect to database
connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


def run_query(title, query):
    print(f"\n--- {title} ---")
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)


# Query 1: Display all records
run_query(
    "All Sales Records",
    "SELECT * FROM sales"
)

# Query 2: Count total records
run_query(
    "Total Records",
    "SELECT COUNT(*) FROM sales"
)

# Query 3: Calculate total revenue
run_query(
    "Total Revenue",
    "SELECT SUM(TotalAmount) FROM sales"
)

# Query 4: Sales by category
run_query(
    "Sales by Category",
    """
    SELECT Category, SUM(TotalAmount)
    FROM sales
    GROUP BY Category
    """
)

# Query 5: Sales by region
run_query(
    "Sales by Region",
    """
    SELECT Region, SUM(TotalAmount)
    FROM sales
    GROUP BY Region
    ORDER BY SUM(TotalAmount) DESC
    """
)

# Query 6: Top-selling products by quantity
run_query(
    "Product Quantity Summary",
    """
    SELECT Product, SUM(Quantity) AS TotalQuantity
    FROM sales
    GROUP BY Product
    ORDER BY TotalQuantity DESC
    """
)

connection.close()
