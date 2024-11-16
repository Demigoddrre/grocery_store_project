import menu_functions
from utils import safe_input

def main_menu():
    while True:
        print("\n=== Grocery Store Management Console ===")
        print("1. Run Stored Procedure")
        print("2. Query Data")
        print("3. Update Customer Details")
        print("4. Update Order Details")
        print("5. Exit")
        choice = safe_input("Enter your choice: ", int)

        if choice == 1:
            run_stored_procedure_menu()
        elif choice == 2:
            query_data_menu()
        elif choice == 3:
            update_customer_menu()
        elif choice == 4:
            update_order_menu()
        elif choice == 5:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def run_stored_procedure_menu():
    print("\n=== Run Stored Procedure ===")
    print("1. Update Inventory After Purchase")
    print("2. Calculate Loyalty Points")
    procedure_choice = safe_input("Select a procedure to run: ", int)

    if procedure_choice == 1:
        product_id = safe_input("Enter Product ID: ", int)
        quantity = safe_input("Enter Quantity: ", int)
        menu_functions.run_procedure("UpdateInventoryAfterPurchase", (product_id, quantity))
    elif procedure_choice == 2:
        customer_id = safe_input("Enter Customer ID: ", int)
        total_amount = safe_input("Enter Total Amount: ", float)
        menu_functions.run_procedure("CalculateLoyaltyPoints", (customer_id, total_amount))
    else:
        print("Invalid choice. Returning to main menu.")

def query_data_menu():
    print("\n=== Query Data ===")
    query = input("Enter your SQL query: ")
    menu_functions.query_data(query)

def update_customer_menu():
    print("\n=== Update Customer Details ===")
    customer_id = safe_input("Enter Customer ID: ", int)
    new_email = input("Enter new email (leave blank to skip): ")
    new_loyalty_points = safe_input("Enter new loyalty points (leave blank to skip): ", int, None)
    menu_functions.update_customer(customer_id, new_email or None, new_loyalty_points)

def update_order_menu():
    print("\n=== Update Order Details ===")
    order_id = safe_input("Enter Order ID: ", int)
    new_total_amount = safe_input("Enter new total amount (leave blank to skip): ", float, None)
    menu_functions.update_order(order_id, new_total_amount)

if __name__ == "__main__":
    main_menu()
