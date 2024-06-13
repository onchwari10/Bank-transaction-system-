import click
from models import Customer, Account, init_db
from database import get_session


Session = get_session()

@click.group()
def cli():
    pass

@click.command()
@click.option('--name', prompt='Customer name', help='Name of the customer.')
@click.option('--email', prompt='Customer email', help='Email of the customer.')
def create_customer(name, email):
    session = Session()
    new_customer = Customer(name=name, email=email)
    session.add(new_customer)
    session.commit()
    click.echo(f'Customer {name} created successfully.')

@click.command()
@click.option('--account_number', prompt='Account number', help='Account number.')
@click.option('--customer_id', prompt='Customer ID', help='ID of the customer owning the account.')
def create_account(account_number, customer_id):
    session = Session()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if not customer:
        click.echo('Customer not found.')
        return
    new_account = Account(account_number=account_number, customer=customer)
    session.add(new_account)
    session.commit()
    click.echo(f'Account {account_number} created successfully.')

@click.command()
def list_customers():
    session = Session()
    customers = session.query(Customer).all()
    for customer in customers:
        click.echo(customer)

@click.command()
@click.option('--customer_id', prompt='Customer ID', help='ID of the customer to view accounts for.')
def view_accounts(customer_id):
    session = Session()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if not customer:
        click.echo('Customer not found.')
        return
    for account in customer.accounts:
        click.echo(account)

@click.command()
@click.option('--customer_id', prompt='Customer ID', help='ID of the customer to delete.')
def delete_customer(customer_id):
    session = Session()
    customer = session.query(Customer).filter_by(id=customer_id).first()
    if not customer:
        click.echo('Customer not found.')
        return
    session.delete(customer)
    session.commit()
    click.echo(f'Customer {customer_id} deleted successfully.')

cli.add_command(create_customer)
cli.add_command(create_account)
cli.add_command(list_customers)
cli.add_command(view_accounts)
cli.add_command(delete_customer)

if __name__ == '__main__':
    cli()
