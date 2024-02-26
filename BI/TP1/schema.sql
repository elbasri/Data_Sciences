CREATE DATABASE IF NOT EXISTS bi;
USE bi;

CREATE TABLE IF NOT EXISTS supermarket_sales (
    InvoiceID VARCHAR(50) PRIMARY KEY,
    Branch CHAR(1),
    City VARCHAR(50),
    CustomerType VARCHAR(50),
    Gender VARCHAR(10),
    ProductLine VARCHAR(100),
    UnitPrice DECIMAL(10, 2),
    Quantity INT,
    Tax5Percent DECIMAL(10, 2),
    Total DECIMAL(10, 2),
    SaleDate DATE,
    SaleTime TIME,
    Payment VARCHAR(50),
    COGS DECIMAL(10, 2),
    GrossMarginPercentage DECIMAL(5, 2),
    GrossIncome DECIMAL(10, 2),
    Rating DECIMAL(3, 1),
    Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
