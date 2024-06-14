import click
from models import Customer, Account
from database import get_session

@click.group()
def cli():
    pass

@click.command()
def create_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    session = get_session()
    new_customer = Customer(name=name, email=email)
    session.add(new_customer)
    session.commit()
    print(f"Customer {name} added successfully!")

@click.command()
def create_account():
    account_number = input("Enter account number: ")
    customer_id = int(input("Enter customer ID: "))
    session = get_session()
    customer = session.query(Customer).get(customer_id)
    if customer:
        new_account = Account(account_number=account_number, customer=customer)
        session.add(new_account)
        session.commit()
        print(f"Account {account_number} added successfully!")
    else:
        print(f"No customer found with ID {customer_id}")

@click.command()
def list_customers():
    session = get_session()
    customers = session.query(Customer).all()
    for customer in customers:
        print(f"ID: {customer.id}, Name: {customer.name}, Email: {customer.email}")

@click.command()
def view_accounts():
    customer_id = int(input("Enter customer ID: "))
    session = get_session()
    customer = session.query(Customer).get(customer_id)
    if customer:
        accounts = customer.accounts
        for account in accounts:
            print(f"Account Number: {account.account_number}, Balance: {account.balance}")
    else:
        print(f"No customer found with ID {customer_id}")

@click.command()
def delete_customer():
    customer_id = int(input("Enter customer ID: "))
    session = get_session()
    customer = session.query(Customer).get(customer_id)
    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer with ID {customer_id} deleted successfully!")
    else:
        print(f"No customer found with ID {customer_id}")

cli.add_command(create_customer)
cli.add_command(create_account)
cli.add_command(list_customers)
cli.add_command(view_accounts)
cli.add_command(delete_customer)

if __name__ == '__main__':
    cli()
