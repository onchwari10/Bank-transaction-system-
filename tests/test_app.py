import pytest
from models import Customer, Account, init_db
from database import get_session

Session = get_session()

@pytest.fixture(scope='module')
def setup_database():
    session = Session()
    init_db()
    yield session
    session.close()

def test_create_customer(setup_database):
    session = setup_database
    new_customer = Customer(name='John Doe', email='john@example.com')
    session.add(new_customer)
    session.commit()
    assert new_customer in session.query(Customer).all()

def test_create_account(setup_database):
    session = setup_database
    customer = session.query(Customer).filter_by(email='john@example.com').first()
    new_account = Account(account_number='123456', customer=customer)
    session.add(new_account)
    session.commit()
    assert new_account in session.query(Account).all()
