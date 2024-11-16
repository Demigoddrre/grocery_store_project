import os
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        database=os.getenv("MYSQL_DATABASE", "grocery_store"),
        user=os.getenv("MYSQL_USER", "admin"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        host=os.getenv("MYSQL_HOST", "mysql"),  # Docker network alias
        port=int(os.getenv("MYSQL_PORT", 3306))
    )
