from config import connect_to_db

def create_tables():
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # SQL statements to create tables with MySQL syntax
    create_products_table = """
    CREATE TABLE IF NOT EXISTS Products (
        ProductID INT AUTO_INCREMENT PRIMARY KEY,
        ProductName VARCHAR(50) NOT NULL,
        Category VARCHAR(50),
        Price DECIMAL(10, 2) NOT NULL,
        StockQuantity INT NOT NULL,
        SupplierID INT,
        FOREIGN KEY (SupplierID) REFERENCES Suppliers(SupplierID) ON DELETE SET NULL
    ) ENGINE=InnoDB;
    """
    
    create_customers_table = """
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INT AUTO_INCREMENT PRIMARY KEY,
        FirstName VARCHAR(50) NOT NULL,
        LastName VARCHAR(50) NOT NULL,
        Email VARCHAR(100) UNIQUE,
        LoyaltyPoints INT DEFAULT 0
    ) ENGINE=InnoDB;
    """
    
    create_orders_table = """
    CREATE TABLE IF NOT EXISTS Orders (
        OrderID INT AUTO_INCREMENT PRIMARY KEY,
        CustomerID INT,
        OrderDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        TotalAmount DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID) ON DELETE CASCADE
    ) ENGINE=InnoDB;
    """
    
    create_orderdetails_table = """
    CREATE TABLE IF NOT EXISTS OrderDetails (
        OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
        OrderID INT,
        ProductID INT,
        Quantity INT NOT NULL,
        Price DECIMAL(10, 2) NOT NULL,
        FOREIGN KEY (OrderID) REFERENCES Orders(OrderID) ON DELETE CASCADE,
        FOREIGN KEY (ProductID) REFERENCES Products(ProductID) ON DELETE CASCADE
    ) ENGINE=InnoDB;
    """
    
    create_suppliers_table = """
    CREATE TABLE IF NOT EXISTS Suppliers (
        SupplierID INT AUTO_INCREMENT PRIMARY KEY,
        SupplierName VARCHAR(50) NOT NULL,
        ContactInfo VARCHAR(100)
    ) ENGINE=InnoDB;
    """
    
    # Execute table creation SQL commands
    cursor.execute(create_suppliers_table)
    cursor.execute(create_products_table)
    cursor.execute(create_customers_table)
    cursor.execute(create_orders_table)
    cursor.execute(create_orderdetails_table)
    
    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    print("Tables created successfully.")

# Run this script to create tables
if __name__ == "__main__":
    create_tables()
