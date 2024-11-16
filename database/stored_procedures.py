from config import connect_to_db

def create_update_inventory_procedure():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Define the MySQL procedure for updating inventory
    update_inventory_procedure = """
    DELIMITER $$
    CREATE PROCEDURE UpdateInventoryAfterPurchase(IN p_ProductID INT, IN p_Quantity INT)
    BEGIN
        UPDATE Products
        SET StockQuantity = StockQuantity - p_Quantity
        WHERE ProductID = p_ProductID;
    END$$
    DELIMITER ;
    """

    # Execute the procedure creation command
    cursor.execute(update_inventory_procedure)
    conn.commit()
    cursor.close()
    conn.close()
    print("Stored procedure for updating inventory created successfully.")

def create_loyalty_points_procedure():
    conn = connect_to_db()
    cursor = conn.cursor()

    # Define the MySQL procedure for calculating loyalty points
    calculate_loyalty_points_procedure = """
    DELIMITER $$
    CREATE PROCEDURE CalculateLoyaltyPoints(IN p_CustomerID INT, IN p_TotalAmount DECIMAL(10, 2))
    BEGIN
        DECLARE new_points INT;
        SET new_points = FLOOR(p_TotalAmount / 10); -- 1 point per $10 spent
        UPDATE Customers
        SET LoyaltyPoints = LoyaltyPoints + new_points
        WHERE CustomerID = p_CustomerID;
    END$$
    DELIMITER ;
    """

    # Execute the procedure creation command
    cursor.execute(calculate_loyalty_points_procedure)
    conn.commit()
    cursor.close()
    conn.close()
    print("Stored procedure for calculating loyalty points created successfully.")

# Run this script to create stored procedures
if __name__ == "__main__":
    create_update_inventory_procedure()
    create_loyalty_points_procedure()
