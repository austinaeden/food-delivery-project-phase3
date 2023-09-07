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
   ```

2. Install the required Python packages.

   ```bash
    pip install faker
    alembic init migrations
    cd lib
    alembic revision -m "empty init"
    alembic upgrade head
    alembic revision --autogenerate -m "created tables"
    alembic upgrade head
   ```

3. Create the SQLite database and populate it with initial data.

   ```bash
   python seed.py
   ```

## Contribution 
Thank you for considering contributing to our project! We welcome contributions of all kinds, including bug reports, feature requests, documentation updates, and code contributions.

To contribute to the project, please follow these steps:

Fork the repository.
Make your changes.
Submit a pull request.

## License
MIT License 
Copyright (c) [2023] [Austin Mbogo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author
This project was created by Austin Mbogo. You can contact me at (austin.mbogo@student.moringaschool.com).

## Support
For help, you can contact (austin.mbogo@student.moringaschool.com).