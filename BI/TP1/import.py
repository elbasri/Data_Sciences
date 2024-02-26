#pip install pandas sqlalchemy mysql-connector-python
import pandas as pd
from sqlalchemy import create_engine

# Replace these values with your actual database connection details
user = 'bi '
password = 'NACER123bi***'
host = 'localhost'
database = 'bi'

# Creating a connection string
connection_string = f"mysql+mysqlconnector://{user}:{password}@{host}/{database}"

# Creating the engine
engine = create_engine(connection_string)

# Load the CSV file into a DataFrame
csv_file_path = 'data/sales/supermarket_sales.csv'
df = pd.read_csv(csv_file_path)

# Rename DataFrame columns to match the database schema
df.columns = ['InvoiceID', 'Branch', 'City', 'CustomerType', 'Gender', 'ProductLine', 
              'UnitPrice', 'Quantity', 'Tax5Percent', 'Total', 'SaleDate', 'SaleTime', 
              'Payment', 'COGS', 'GrossMarginPercentage', 'GrossIncome', 'Rating']

# Convert SaleDate and SaleTime to a single datetime column if necessary
# This step is optional and depends on your specific requirements
df['SaleDate'] = pd.to_datetime(df['SaleDate'] + ' ' + df['SaleTime'])
df.drop('SaleTime', axis=1, inplace=True)

# Insert data into the database
df.to_sql('supermarket_sales', con=engine, if_exists='append', index=False)


print("Data imported successfully.")

