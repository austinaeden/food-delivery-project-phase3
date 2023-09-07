markdown
Copy code
# Food Delivery Application

This repository contains a Python-based food delivery application that manages customers, restaurants, menu items, orders, and ordered items. The application utilizes SQLAlchemy for database management and Click for building a Command-Line Interface (CLI) to interact with the system.

## Files

### `app.py`

`app.py` defines the SQLAlchemy models and the database schema for the food delivery application. It includes the following classes:

- `Customer`: Represents a customer with attributes like `cus_id` and `username`.
- `Restaurant`: Represents a restaurant with attributes like `res_id`, `name`, and `location`.
- `MenuItem`: Represents a menu item with attributes like `item_id`, `name`, `price`, and `description`.
- `Order`: Represents an order with attributes like `order_id`, `customer_id`, and `restaurant_id`.
- `OrderedItem`: Represents an ordered item with attributes like `item_id`, `menu_item_id`, `order_id`, and `quantity`.

The file also establishes a connection to the SQLite database using SQLAlchemy.

### `seed.py`

`seed.py` is a script used for seeding initial data into the food delivery application's database. It utilizes the Faker library to generate mock customer data. It creates customers, restaurants, menu items, orders, and ordered items and populates the database with this data.

## Prerequisites

Before using the food delivery application, make sure you have the following dependencies installed:

- Python 3.x
- SQLAlchemy
- Faker (for seeding data)

## Usage

1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/austinaeden/food-delivery-project-phase3.git

2. Install the required Python packages.

    ```bash
    Copy code
    pip install -r requirements.txt

3. Create the SQLite database and populate it with initial data.

    ```bash
    Copy code
    python seed.py

4. Run the application to interact with the database and manage customer orders.

    ```bash
    Copy code
    python restaurant.py

## Example Output
When you run the application, you will see the following output:

    ```bash
    Copy code
    [Orange]Customers:[Reset]
    [Green] Username: customer1[Reset]
    [Green] Username: customer2[Reset]
    [Green] Username: customer3[Reset]

    [Orange]
    Restaurants:[Reset]
    [Green] Name: Restaurant A, Location: Location A[Reset]
    [Green] Name: Restaurant B, Location: Location B[Reset]
    [Green] Name: Restaurant C, Location: Location C[Reset]

    [Orange]
    Menu Items:[Reset]
    [Green] Name: Item 1, Price: 10[Reset]
    [Green] Name: Item 2, Price: 15[Reset]
    [Green] Name: Item 3, Price: 20[Reset]

    [Orange]
    Orders:[Reset]
    [Green] Order ID: 1, Customer: customer1, Restaurant: Restaurant A[Reset]
    [Green] Order ID: 2, Customer: customer2, Restaurant: Restaurant B[Reset]
    [Green] Order ID: 3, Customer: customer3, Restaurant: Restaurant C[Reset]

    [Orange]
    Ordered Items:[Reset]
    [Green] Order Item ID: 1, Menu Item: Item 1, Quantity: 2[Reset]
    [Green] Order Item ID: 2, Menu Item: Item 2, Quantity: 3[Reset]
    [Green] Order Item ID: 3, Menu Item: Item 3, Quantity: 1[Reset]


## Contribution
Thank you for considering contributing to our project! We welcome contributions of all kinds, including bug reports, feature requests, documentation updates, and code contributions.

To contribute to the project, please follow these steps:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
This project was created by Austin Mbogo. You can contact me at austin.mbogo@student.moringaschool.com.

## Support
For help, you can contact austin.mbogo@student.moringaschool.com.

    ```bash
    Copy code

    You can create a `README.md` file in your project's repository and paste this content into it.
