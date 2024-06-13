from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    
    accounts = relationship('Account', back_populates='customer', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Customer(name={self.name}, email={self.email})>'

class Account(Base):
    __tablename__ = 'accounts'
    
    id = Column(Integer, primary_key=True)
    account_number = Column(String, nullable=False, unique=True)
    balance = Column(Float, default=0.0)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    
    customer = relationship('Customer', back_populates='accounts')
    
    def __repr__(self):
        return f'<Account(account_number={self.account_number}, balance={self.balance})>'

def init_db():
    engine = create_engine('sqlite:///bank.db')
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)
