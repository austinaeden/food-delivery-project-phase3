# Importing dependencies from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base 

# Define the database connection
DATABASE_URI = 'sqlite:///food_delivery.db'  # the path to the database
engine = create_engine(DATABASE_URI, echo=True)  # Creating a database engine with echoing enabled for debugging

# Base class for all the classes
Base = declarative_base()  

# Creating tables for the 'customer' table
class Customer(Base):
    __tablename__ = 'customer'
    cus_id = Column(Integer, Sequence('cus_id_seq'), primary_key=True)  # Primary key for the customer table
    username = Column(String)  # Column for storing customer usernames
    
    orders = relationship("Order", back_populates="customer")  # Relationship to orders table

    # String representation of a customer object
    def __repr__(self):
        return f"Username: {self.username}"
    
    # Method to return a list of orders associated with this customer
    def orders_list(self):
        return [order for order in self.orders]

    def add_order(self, restaurant, menu_items):
        # Create a new order for this customer and restaurant
        order = Order(customer=self, restaurant=restaurant)
        session.add(order)
        
        # Add ordered items to the order
        for menu_item, quantity in menu_items.items():
            ordered_item = OrderedItem(menu_item=menu_item, order=order, quantity=quantity)
            session.add(ordered_item)
        
        # Commit the changes to the database
        session.commit()

    def remove_order(self, order):
        # Remove the order and its associated ordered items
        session.delete(order)
        
        # Commit the changes to the database
        session.commit()

# Creating a table for the 'restaurant' table
class Restaurant(Base):
    __tablename__ = 'restaurant'
    res_id = Column(Integer, Sequence('res_id_seq'), primary_key=True)  # Primary key for the restaurant table
    name = Column(String)  # Column for storing restaurant names
    location = Column(String)  # Column for storing restaurant locations
    
    # Relationships to menu items and orders tables
    menu_items = relationship("MenuItem", back_populates="restaurant")
    orders = relationship("Order", back_populates="restaurant")

    # String representation of a restaurant object
    def __repr__(self):
        return f"Name: {self.name}, Location: {self.location}"
    
    # Method to return a list of menu items associated with this restaurant
    def menu_items_list(self):
        return [menu_item for menu_item in self.menu_items]

# Creating a table for the 'menu_item' table
class MenuItem(Base):
    __tablename__ = 'menu_item'
    item_id = Column(Integer, Sequence('item_id_seq'), primary_key=True)  # Primary key for the menu_item table
    name = Column(String)  # Column for storing menu item names
    price = Column(Integer)  # Column for storing menu item prices
    description = Column(String)  # Column for storing menu item descriptions
    restaurant_id = Column(Integer, ForeignKey('restaurant.res_id'))  # Foreign key to link menu items to restaurants
    
    # Relationships to restaurant and ordered items tables
    restaurant = relationship("Restaurant", back_populates="menu_items")
    ordered_items = relationship("OrderedItem", back_populates="menu_item")
    
    # String representation of a menu item object
    def __repr__(self):
        return f"Name: {self.name}, Price: {self.price}"

# Creating a table for the 'order' table
class Order(Base):
    __tablename__ = 'order'
    order_id = Column(Integer, Sequence('order_id_seq'), primary_key=True)  # Primary key for the order table
    customer_id = Column(Integer, ForeignKey('customer.cus_id'))  # Foreign key to link orders to customers
    restaurant_id = Column(Integer, ForeignKey('restaurant.res_id'))  # Foreign key to link orders to restaurants
    
    # Relationships to customer, restaurant, and ordered items tables
    customer = relationship("Customer", back_populates="orders")
    restaurant = relationship("Restaurant", back_populates="orders")
    ordered_items = relationship("OrderedItem", back_populates="order")
    
    # String representation of an order object
    def __repr__(self):
        return f"Order ID: {self.order_id}, Customer: {self.customer.username}, Restaurant: {self.restaurant.name}"

# Creating a table for the 'ordered_item' table
class OrderedItem(Base):
    __tablename__ = 'ordered_item'
    item_id = Column(Integer, Sequence('item_id_seq'), primary_key=True)  # Primary key for the ordered_item table
    menu_item_id = Column(Integer, ForeignKey('menu_item.item_id'))  # Foreign key to link ordered items to menu items
    order_id = Column(Integer, ForeignKey('order.order_id'))  # Foreign key to link ordered items to orders
    quantity = Column(Integer)  # Column for storing item quantities
    
    # Relationships to the menu items and orders tables
    menu_item = relationship("MenuItem", back_populates="ordered_items")
    order = relationship("Order", back_populates="ordered_items")
    
    # String representation of an ordered item object
    def __repr__(self):
        return f"Order Item ID: {self.item_id}, Menu Item: {self.menu_item.name}, Quantity: {self.quantity}"

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


# Define ANSI escape codes for text colors
GREEN = '\033[92m'  # Green text color
RESET = '\033[0m'    # Reset text color to default

if __name__ == '__main__':
    customer = session.query(Customer).filter_by(username="customer1").first()
    restaurant = session.query(Restaurant).filter_by(name="Restaurant A").first()
    menu_item_1 = session.query(MenuItem).filter_by(name="Item 1").first()
    menu_item_2 = session.query(MenuItem).filter_by(name="Item 2").first()

    # Add an order for the customer
    menu_items = {
        menu_item_1: 2,
        menu_item_2: 1,
    }
    if customer:
        customer.add_order(restaurant, menu_items)
        print(f"{GREEN}Order added for customer.{RESET}")
    else:
        print("Customer not found.")

    # Print the customer's orders
    print(f"{GREEN}Customer: {customer.username}'s Orders:{RESET}")
    for order in customer.orders:
        print(f"{GREEN}Order ID: {order.order_id}, Restaurant: {order.restaurant.name}{RESET}")
        print(f"{GREEN}Ordered Items:{RESET}")
        for ordered_item in order.ordered_items:
            print(f" {GREEN} Menu Item: {ordered_item.menu_item.name}, Quantity: {ordered_item.quantity}{RESET}")

    # Remove an order for the customer
    order_to_remove = customer.orders[0]
    customer.remove_order(order_to_remove)
    print(f"{GREEN}Order removed for customer.{RESET}")

