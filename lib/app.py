# alembic upgrade head
# pip install faker
# alembic init migrations
# cd lib
# alembic revision -m "empty init"
# alembic upgrade head
# alembic revision --autogenerate -m "created tables"
# alembic upgrade head

from sqlalchemy import create_engine, Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection
DATABASE_URI = 'sqlite:///food_delivery.db'  # the path to the database
engine = create_engine(DATABASE_URI, echo=True)

# Base class for all the classes
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    cus_id = Column(Integer, Sequence('cus_id_seq'), primary_key=True)
    username = Column(String)
    
    orders = relationship("Order", back_populates="customer")

    

# Create session
Session = sessionmaker(bind=engine)
session = Session()
