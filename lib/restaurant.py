# Importing dependencies from SQLAlchemy
from app import Customer, Restaurant, MenuItem, Order, OrderedItem, Session
import click
from sqlalchemy.orm import sessionmaker
ORANGE = '\033[93m'  # Orange text color
GREEN = '\033[92m'  # Green text color
RESET = '\033[0m'    # Reset text color to default

def print_all_data(session):
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

def add_customer_order(session, customer_username):
    customer = session.query(Customer).filter_by(username=customer_username).first()
    
    if customer:
        print(f"{GREEN}Customer found:{RESET}")
        print(f"{GREEN}{customer}{RESET}")

        # Detach the customer object from the current session if it's attached
        if session.is_active:
            session.expunge(customer)
        
        # Prompt the user for restaurant name
        restaurant_name = input("Enter restaurant name: ")
        
        # Detach the restaurant object from the current session if it's attached
        restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
        if restaurant:
            session.expunge(restaurant)
        
        if restaurant:
            print(f"{GREEN}Restaurant found:{RESET}")
            print(f"{GREEN}{restaurant}{RESET}")

            # Prompt the user for menu items and quantities
            menu_items = {}
            try:
                while True:
                    item_name = input("Enter menu item name (or leave empty to finish): ")
                    if not item_name:
                        break
                    menu_item = session.query(MenuItem).filter_by(name=item_name).first()
                    if menu_item:
                        # Detach the menu item object from the current session if it's attached
                        session.expunge(menu_item)
                        
                        quantity = int(input(f"Enter quantity for {item_name}: "))
                        menu_items[menu_item] = quantity
                    else:
                        print(f"{GREEN}Menu item not found.{RESET}")

                if menu_items:
                    # Add the order
                    customer.add_order(restaurant, menu_items)
                    print(f"{GREEN}Order added for customer.{RESET}")
                else:
                    print(f"{GREEN}No items added to the order.{RESET}")

            except Exception as e:
                session.rollback()
                print(f"An error occurred: {str(e)}")
            finally:
                session.close()

        else:
            print(f"{GREEN}Restaurant not found.{RESET}")
    else:
        print(f"{GREEN}Customer not found.{RESET}")

def delete_customer_order(session, order_id):
    order_to_delete = session.query(Order).filter_by(order_id=order_id).first()
    
    if order_to_delete:
        customer = order_to_delete.customer
        print(f"{GREEN}Order found for customer:{RESET}")
        print(f"{GREEN}Customer: {customer.username}, Order ID: {order_to_delete.order_id}{RESET}")
        print(f"{GREEN}Ordered Items:{RESET}")
        for ordered_item in order_to_delete.ordered_items:
            print(f"{GREEN} Menu Item: {ordered_item.menu_item.name}, Quantity: {ordered_item.quantity}{RESET}")

        # Prompt for confirmation before deleting
        confirmation = input("Are you sure you want to delete this order? (yes/no): ").lower()
        if confirmation == 'yes':
            customer.orders.remove(order_to_delete)  # Remove the order from the customer's orders collection
            session.delete(order_to_delete)  # Delete the order from the database
            session.commit()  # Commit the changes to the database
            print(f"{GREEN}Order deleted successfully.{RESET}")
        else:
            print("Order deletion cancelled.")
    else:
        print(f"{GREEN}Order not found.{RESET}")


@click.command()
@click.option('--view', is_flag=True, help='View all data')
@click.option('--search', default=None, help='Search for a specific customer by username')
@click.option('--add-order', default=None, help='Add an order for a customer by username')
@click.option('--delete-order', default=None, help='Delete an order for a customer by order ID')
def main(view, search, add_order, delete_order):
    session = Session()
    if view:
        print_all_data(session)
    elif search:
        customer = session.query(Customer).filter_by(username=search).first()
        if customer:
            print(f"{GREEN}Customer found:{RESET}")
            print(f"{GREEN}{customer}{RESET}")
        else:
            print(f"{GREEN}Customer not found.{RESET}")
    elif add_order:
        add_customer_order(session, add_order)
    
    elif delete_order:
        delete_customer_order(session, delete_order)  # Call the new delete function

    # Close the session when done
    session.close()

if __name__ == '__main__':
    main()
