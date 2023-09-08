# Importing dependencies from SQLAlchemy
from app import Customer, Restaurant, MenuItem, Order, OrderedItem, Session
import click
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


@click.command()
@click.option('--view', is_flag=True, help='View all data')
@click.option('--search', default=None, help='Search for a specific customer by username')
@click.option('--add-order', default=None, help='Add an order for a customer by username')
@click.option('--delete-order', default=None, help='Delete an order for a customer by order ID')
def main(view, search, add_order, delete_order):
    if view:
        print_all_data()
    elif search:
        session = Session()
        customer = session.query(Customer).filter_by(username=search).first()
        if customer:
            print(f"{GREEN}Customer found:{RESET}")
            print(f"{GREEN}{customer}{RESET}")
        else:
            print(f"{GREEN}Customer not found.{RESET}")
    elif add_order:
        session = Session()
        customer = session.query(Customer).filter_by(username=add_order).first()
        if customer:
            print(f"{GREEN}Customer found:{RESET}")
            print(f"{GREEN}{customer}{RESET}")

            # Prompt the user for restaurant name
            restaurant_name = input("Enter restaurant name: ")
            restaurant = session.query(Restaurant).filter_by(name=restaurant_name).first()
            
            if restaurant:
                print(f"{GREEN}Restaurant found:{RESET}")
                print(f"{GREEN}{restaurant}{RESET}")

                # Prompt the user for menu items and quantities
                menu_items = {}
                while True:
                    item_name = input("Enter menu item name (or leave empty to finish): ")
                    if not item_name:
                        break
                    menu_item = session.query(MenuItem).filter_by(name=item_name).first()
                    if menu_item:
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
            else:
                print(f"{GREEN}Restaurant not found.{RESET}")
        else:
            print(f"{GREEN}Customer not found.{RESET}")

    elif delete_order:
        session = Session()
        order_to_delete = session.query(Order).filter_by(order_id=delete_order).first()
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
                customer.remove_order(order_to_delete)
                print(f"{GREEN}Order deleted successfully.{RESET}")
            else:
                print("Order deletion cancelled.")
        else:
            print(f"{GREEN}Order not found.{RESET}")


if __name__ == '__main__':
    main()