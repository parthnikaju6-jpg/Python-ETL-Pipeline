
# Python ETL Pipeline

## Project Overview
This project demonstrates a basic ETL (Extract, Transform, Load)
pipeline using Python, Pandas, and SQLite.

The pipeline extracts retail sales data from a CSV file,
cleans and transforms the data, and loads the processed
records into an SQLite database.

## Technologies Used
- Python
- Pandas
- SQLite
- SQL
- Git and GitHub

## Project Structure
- data/: Contains raw sales CSV data
- src/: Contains ETL and database verification scripts
- sales.db: SQLite database
- main.py: Runs the complete ETL pipeline

## ETL Process

### 1. Extract
Reads raw sales data from a CSV file using Pandas.

### 2. Transform
- Removes duplicate records
- Handles missing customer names
- Removes records with invalid quantities
- Converts order dates into datetime format
- Calculates TotalAmount

### 3. Load
Loads the cleaned sales data into an SQLite database
table named sales.

## Database Verification
SQL queries are used to:
- Count total records
- Calculate total revenue
- Summarize sales by category
- Summarize sales by region
- Analyze product quantities

## Sample Results
- Records before cleaning: 13
- Records after cleaning: 11
- Total revenue: ₹3,31,300

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run the ETL pipeline:
   python main.py

3. Verify the database:
   python src/verify_db.py

## Learning Outcomes
- Understanding ETL concepts
- Reading CSV files with Pandas
- Cleaning and transforming data
- Working with SQLite databases
- Writing SQL queries for data analysis
    