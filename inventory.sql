/*
This file contains a script of Transact SQL (T-SQL) command to interact with a database named 'Inventory'.
Requirements:
- SQL Server 2022 is installed and running
- database 'Inventory' already exists.
Details:
- 1) Sets the default database to 'Inventory'.
- 2) Creates a 'categories' table and related 'products' table if they do not already exist.
- 3) Remove all rows from the tables.
- 4) Remove all rows from the tables (in case they already existed).
- 5) Populates the 'Categories' table with sample data.
- 6) Populates the 'Products' table with sample data.
Errors:
- if the database 'Inventory' does not exist, the script will print an error message and exit.
*/

-- check if the 'Inventory' database exists.
IF DB_ID('Inventory') IS NULL
BEGIN
    PRINT 'Error: Database ''Inventory'' does not exist.';
    RETURN;
END;

-- set the default database to 'Inventory'
USE Inventory;

-- create the 'Categories' table if it does not already exist
IF OBJECT_ID('Categories', 'U') IS NULL
BEGIN
    CREATE TABLE Categories
    (
        CategoryID INT PRIMARY KEY,
        CategoryName NVARCHAR(50) NOT NULL
    );
END;

-- create the 'Products' table if it does not already exist
IF OBJECT_ID('Products', 'U') IS NULL
BEGIN
    CREATE TABLE Products
    (
        ProductID INT PRIMARY KEY,
        ProductName NVARCHAR(50) NOT NULL,
        CategoryID INT NOT NULL,
        Price DECIMAL(10, 2) NOT NULL,
        -- add a timestamp column for the date and time the row was created
        CreatedAt DATETIME DEFAULT GETDATE(),
        -- add a timestamp column for the date and time the row was last updated
        UpdatedAt DATETIME DEFAULT GETDATE(),
        FOREIGN KEY (CategoryID) REFERENCES Categories(CategoryID)
    );
END;

-- remove all rows from the 'products' table
TRUNCATE TABLE Products;

-- remove all rows from the 'categories' table
TRUNCATE TABLE Categories;

-- populate the 'Categories' table with sample data
INSERT INTO Categories (CategoryID, CategoryName)
VALUES
    (1, 'Electronics'),
    (2, 'Clothing'),
    (3, 'Books'),
    (4, 'Home Goods'),
    (5, 'Toys'),
    (6, 'Sporting Goods'),
    (7, 'Health & Beauty'),
    (8, 'Food & Beverage');

-- populate the 'Products' table with sample data
INSERT INTO Products (ProductID, ProductName, CategoryID, Price)
VALUES
    (1, 'Smartphone', 1, 599.99),
    (2, 'Laptop', 1, 999.99),
    (3, 'T-Shirt', 2, 19.99),
    (4, 'Jeans', 2, 39.99),
    (5, 'Novel', 3, 14.99),
    (6, 'Cookbook', 3, 24.99),
    (7, 'Candle', 4, 9.99),
    (8, 'Picture Frame', 4, 29.99),
    (9, 'Action Figure', 5, 12.99),
    (10, 'Board Game', 5, 24.99),
    (11, 'Basketball', 6, 29.99),
    (12, 'Yoga Mat', 6, 19.99),
    (13, 'Shampoo', 7, 7.99);


-- Create a stored procedure 'RetrieveAllCategories' to get all categories.
IF OBJECT_ID('RetrieveAllCategories', 'P') IS NOT NULL
BEGIN
    DROP PROCEDURE RetrieveAllCategories;
END;

-- Create a stored procedure 'ProductsByCategory' to get all products in a specific category.
IF OBJECT_ID('ProductsInInventoryByCategory', 'P') IS NOT NULL
BEGIN
    DROP PROCEDURE ProductsInInventoryByCategory;
END;

-- Create a stored procedure 'CreateProduct' to insert a new product into the 'Products' table.



