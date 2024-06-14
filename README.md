Overview
The Bank Transaction System is a Python CLI application that allows users to manage bank customers and their accounts. The system uses SQLAlchemy ORM for database interactions and provides functionalities such as creating customers, creating accounts, listing customers, viewing accounts, and deleting customers.

Features
Create and manage bank customers
Create and manage bank accounts
List all customers
View accounts associated with a specific customer
Delete customers
Requirements
Python 3.10+
Pipenv
Setup
Clone the repository:



Project Structure

Bank-transaction-system/
│
├── models.py              # Contains the Customer and Account ORM models
├── database.py            # Contains database setup and session creation
├── app.py                 # Initializes the database
├── cli.py                 # CLI application for managing customers and accounts
├── Pipfile                # Pipenv configuration file
├── Pipfile.lock           # Pipenv lock file
└── README.md              # Project documentation