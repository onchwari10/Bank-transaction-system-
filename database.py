# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create engine
engine = create_engine('sqlite:///bank.db')

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a session
def get_session():
    return Session()
