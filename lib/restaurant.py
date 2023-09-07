# Importing dependencies from SQLAlchemy
from app import Customer, Restaurant, MenuItem, Order, OrderedItem, Session
ORANGE = '\033[93m'  # Orange text color
GREEN = '\033[92m'  # Green text color
RESET = '\033[0m'    # Reset text color to defaul

def print_all_data():
    # Create a session to interact with the database
    session = Session()

    # Print all customers
    print(f"{ORANGE}Customers:{RESET}")
    for customer in session.query(Customer).all():
        print(f" {GREEN} {customer}{RESET}")

    # Print all restaurants
    print(f"{ORANGE}\nRestaurants:{RESET}")
    for restaurant in session.query(Restaurant).all():
        print(f" {GREEN} {restaurant}{RESET}")

    # Print all menu items
    print(f"{ORANGE}\nMenu Items:{RESET}")
    for menu_item in session.query(MenuItem).all():
        print(f" {GREEN} {menu_item}{RESET}")

    # Print all orders
    print(f"{ORANGE}\nOrders:{RESET}")
    for order in session.query(Order).all():
        print(f"{GREEN}{order}{RESET}")

    # Print all ordered items
    print(f"{ORANGE}\nOrdered Items:{RESET}")
    for ordered_item in session.query(OrderedItem).all():
        print(f"{GREEN}{ordered_item}{RESET}")

    # Close the session
    session.close()

    

if __name__ == '__main__':
    print_all_data()
