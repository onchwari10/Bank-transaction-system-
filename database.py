from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///bank.db')
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
