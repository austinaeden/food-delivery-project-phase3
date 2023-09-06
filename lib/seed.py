from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import Customer, Restaurant, MenuItem, Order, OrderedItem, Base  # Replace 'app' with the actual module name where your models are defined

fake = Faker()

# Define the database connection
DATABASE_URI = 'sqlite:///food_delivery.db'  # the path to the database
engine = create_engine(DATABASE_URI, echo=True)

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    # Create tables in the database
    Base.metadata.create_all(engine)

    # Create customers
    customers = [
        Customer(username="customer1"),
        Customer(username="customer2"),
        Customer(username="customer3"),
    ]
    session.add_all(customers)

    # Create restaurants
    restaurants = [
        Restaurant(name="Restaurant A", location="Location A"),
        Restaurant(name="Restaurant B", location="Location B"),
        Restaurant(name="Restaurant C", location="Location C"),
    ]
    session.add_all(restaurants)

    # Create menu items for each restaurant
    for restaurant in restaurants:
        menu_items = [
            MenuItem(name="Item 1", price=10, description="Description 1", restaurant=restaurant),
            MenuItem(name="Item 2", price=15, description="Description 2", restaurant=restaurant),
            MenuItem(name="Item 3", price=20, description="Description 3", restaurant=restaurant),
        ]
        session.add_all(menu_items)

    # Create orders
    orders = [
        Order(customer=customers[0], restaurant=restaurants[0]),
        Order(customer=customers[1], restaurant=restaurants[1]),
        Order(customer=customers[2], restaurant=restaurants[2]),
    ]
    session.add_all(orders)

    # Create ordered items for each order
    ordered_items = [
        OrderedItem(menu_item=menu_items[0], order=orders[0], quantity=2),
        OrderedItem(menu_item=menu_items[1], order=orders[1], quantity=3),
        OrderedItem(menu_item=menu_items[2], order=orders[2], quantity=1),
    ]
    session.add_all(ordered_items)

    # Commit the changes to the database
    session.commit()

    print("Data seeded successfully.")
