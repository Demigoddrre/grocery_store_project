from config import connect_to_db
from contextlib import closing
from utils import log_activity, log_error

def run_procedure(procedure_name, params=None):
    """Executes a stored procedure."""
    with closing(connect_to_db()) as conn:
        with conn.cursor() as cursor:
            try:
                if params:
                    cursor.callproc(procedure_name, params)
                else:
                    cursor.callproc(procedure_name)
                conn.commit()
                log_activity(f"Procedure '{procedure_name}' executed successfully.")
            except Exception as e:
                log_error(f"Error executing procedure '{procedure_name}': {e}")

def query_data(query, params=None):
    """Executes a query and prints the results."""
    with closing(connect_to_db()) as conn:
        with conn.cursor() as cursor:
            try:
                cursor.execute(query, params or ())
                rows = cursor.fetchall()
                for row in rows:
                    print(row)
            except Exception as e:
                log_error(f"Error executing query: {e}")

def update_customer(customer_id, new_email=None, new_loyalty_points=None):
    """Updates customer details."""
    with closing(connect_to_db()) as conn:
        with conn.cursor() as cursor:
            try:
                if new_email:
                    cursor.execute("UPDATE Customers SET Email = %s WHERE CustomerID = %s", (new_email, customer_id))
                if new_loyalty_points is not None:
                    cursor.execute("UPDATE Customers SET LoyaltyPoints = %s WHERE CustomerID = %s", (new_loyalty_points, customer_id))
                conn.commit()
                log_activity(f"Customer {customer_id} updated successfully.")
            except Exception as e:
                log_error(f"Error updating customer: {e}")

def update_order(order_id, new_total_amount=None):
    """Updates order details."""
    with closing(connect_to_db()) as conn:
        with conn.cursor() as cursor:
            try:
                if new_total_amount is not None:
                    cursor.execute("UPDATE Orders SET TotalAmount = %s WHERE OrderID = %s", (new_total_amount, order_id))
                conn.commit()
                log_activity(f"Order {order_id} updated successfully.")
            except Exception as e:
                log_error(f"Error updating order: {e}")
