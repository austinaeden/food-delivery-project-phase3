# Import the necessary dependencies
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from app import Customer, Restaurant, MenuItem, Order, OrderedItem, Base

# Create a Faker instance
fake = Faker()

if __name__ == '__main__':
    # Define the database connection
    DATABASE_URI = 'sqlite:///food_delivery.db'  # the path to the database
    engine = create_engine(DATABASE_URI, echo=False)
    
    # Create tables
    Base.metadata.create_all(engine)
    
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create customers with fake usernames
    customers = [
        Customer(username=fake.user_name()) for _ in range(8)
    ]
    session.add_all(customers)

    # Create restaurants with fake names and locations
    restaurants = [
        Restaurant(name=fake.company(), location=fake.address()) for _ in range(3)
    ]
    session.add_all(restaurants)

    # Create menu items for each restaurant with fake names, prices, and descriptions
    for restaurant in restaurants:
        menu_items = [
            MenuItem(
                name=fake.word(),
                price=fake.random_int(min=5, max=30),  # Generate random prices
                description=fake.sentence(),
                restaurant=restaurant,
            ) for _ in range(5)
        ]
        session.add_all(menu_items)

    # Create orders
    orders = [
        Order(customer=fake.random_element(customers), restaurant=fake.random_element(restaurants))
        for _ in range(3)
    ]
    session.add_all(orders)

    # Create ordered items with random quantities for each order
    ordered_items = [
        OrderedItem(
            menu_item=fake.random_element(menu_items),
            order=fake.random_element(orders),
            quantity=fake.random_int(min=1, max=5),  # Generate random quantities
        ) for _ in range(3)
    ]
    session.add_all(ordered_items)

    # Commit the changes to the database
    session.commit()

    print("Data seeded successfully.")
