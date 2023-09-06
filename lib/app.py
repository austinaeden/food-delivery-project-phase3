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

    def __repr__(self):
        return f"Username: {self.username}"
    
    def orders_list(self):
        return [order for order in self.orders]

class Restaurant(Base):
    __tablename__ = 'restaurant'
    res_id = Column(Integer, Sequence('res_id_seq'), primary_key=True)
    name = Column(String)
    location = Column(String)
    
    menu_items = relationship("MenuItem", back_populates="restaurant")
    orders = relationship("Order", back_populates="restaurant")

    def __repr__(self):
        return f"Name: {self.name}, Location: {self.location}"
    
    def menu_items_list(self):
        return [menu_item for menu_item in self.menu_items]

class MenuItem(Base):
    __tablename__ = 'menu_item'
    item_id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurant.res_id'))
    
    restaurant = relationship("Restaurant", back_populates="menu_items")
    ordered_items = relationship("OrderedItem", back_populates="menu_item")

    def __repr__(self):
        return f"Name: {self.name}, Price: {self.price}"

class Order(Base):
    __tablename__ = 'order'
    order_id = Column(Integer, Sequence('order_id_seq'), primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.cus_id'))
    restaurant_id = Column(Integer, ForeignKey('restaurant.res_id'))
    
    customer = relationship("Customer", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")
    ordered_items = relationship("OrderedItem", back_populates="order")

    def __repr__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.username}, Restaurant: {self.restaurant.name}"

class OrderedItem(Base):
    __tablename__ = 'ordered_item'
    item_id = Column(Integer, Sequence('item_id_seq'), primary_key=True)
    menu_item_id = Column(Integer, ForeignKey('menu_item.item_id'))
    order_id = Column(Integer, ForeignKey('order.order_id'))
    quantity = Column(Integer)

    menu_item = relationship("MenuItem", back_populates="ordered_items")
    order = relationship("Order", back_populates="ordered_items")

    def __repr__(self):
        return f"Order Item ID: {self.item_id}, Menu Item: {self.menu_item.name}, Quantity: {self.quantity}"

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Test add_review and delete_review methods
# customer1 = session.query(Customer).filter_by(cus_id=20).first()  # Change cus_id to the desired customer
# print(customer1.delete_review(42))
# customer2 = session.query(Customer).filter_by(cus_id=10).first()  # Change cus_id to the desired customer
# print(customer2.add_review(18, 5))

