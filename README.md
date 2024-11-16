# Grocery Store Management System

A console-based application for managing a grocery store's operations, including inventory updates, loyalty points calculation, and customer and order management. The application uses **Python**, **MySQL**, and **Docker** for a scalable and modular design.

---

## Features

- **Inventory Management**: Automatically updates stock quantities after purchases.
- **Loyalty Points System**: Calculates and updates loyalty points based on order totals.
- **Customer Management**: Update customer details such as email and loyalty points.
- **Order Management**: Modify order details, including total amounts.
- **Query Data**: Run custom SQL queries directly from the console.
- **Modular Design**: Uses stored procedures for reusable business logic.

---

## Prerequisites

- Docker and Docker Compose installed on your system.
- Python 3.12 or higher (for development purposes).
- MySQL 8.0.

---

## Project Structure

grocery_store_project/ │ ├── database/ │ ├── create_tables.py # Creates the database schema │ ├── stored_procedures.py # Defines and sets up stored procedures │ └── config.py # Database connection configuration │ ├── utils/ │ └── utils.py # Helper functions for input validation and table formatting │ ├── main.py # Main menu for the console application ├── menu_functions.py # Functions to handle menu actions ├── Dockerfile # Docker configuration for the Python application ├── docker-compose.yml # Docker Compose configuration ├── requirements.txt # Python dependencies └── README.md # Project documentation


Copy code

---

## Installation and Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Demigoddrre/grocery_store_project.git
cd grocery_store_project
2. Build and Start the Application
Using Docker Compose:

bash
Copy code
docker-compose up --build
3. Access the Application
Once the services are running, you can interact with the application through the console by executing:

bash
Copy code
docker exec -it grocery_app python main.py
Configuration
Environment Variables
The project uses the following environment variables (configured in docker-compose.yml):

MYSQL_DATABASE: Database name (default: grocery_store).
MYSQL_USER: Database user (default: admin).
MYSQL_PASSWORD: User password (default: password).
MYSQL_ROOT_PASSWORD: Root password for MySQL (default: rootpassword).
Usage
Main Menu
Run Stored Procedure
Update Inventory After Purchase
Calculate Loyalty Points
Query Data
Run custom SQL queries.
Update Customer Details
Modify customer email or loyalty points.
Update Order Details
Change total order amounts.
Database Schema
Tables
Products
Customers
Orders
OrderDetails
Suppliers
Stored Procedures
UpdateInventoryAfterPurchase: Adjusts inventory after a purchase.
CalculateLoyaltyPoints: Adds loyalty points based on total order amounts.
Requirements
Python Packages (listed in requirements.txt):
mysql-connector-python==8.0.33
Known Issues
Ensure the database container is healthy before running the application (service_healthy in docker-compose.yml).
If tables are not created, verify database connection parameters in config.py.
Contributing
Fork the repository.
Create a new branch (git checkout -b feature-name).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-name).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Special thanks to the contributors and open-source projects that made this application possible.

markdown
Copy code

### Summary of Updates:
- Clear explanation of project features, setup, and usage.
- Detailed instructions for running the application with Docker.
- Description of database schema and stored procedures.
- Includes contribution guidelines and licensing information.

Let me know if you'd like further refinements!