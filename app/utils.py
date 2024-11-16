from mysql.connector import connect, Error
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_db_connection():
    """Creates and returns a new MySQL database connection."""
    try:
        conn = connect(
            host=os.getenv("MYSQL_HOST", "localhost"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "password"),
            database=os.getenv("MYSQL_DATABASE", "grocery_store")
        )
        return conn
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def safe_input(prompt, cast_type=str, default=None):
    """Gets a safe input with optional type conversion."""
    try:
        return cast_type(input(prompt))
    except ValueError:
        print(f"Invalid input. Returning default value: {default}")
        return default

def format_table(headers, rows):
    """Formats and prints a table given headers and rows."""
    print(f"\n{' | '.join(headers)}")
    print('-' * (len(headers) * 15))
    for row in rows:
        print(' | '.join(str(col) for col in row))
    print("\n")

def log_activity(message):
    logging.info(message)

def log_error(message):
    logging.error(message)
