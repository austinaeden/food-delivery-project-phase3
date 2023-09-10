# Restaurant Order Management System

This Python project is a restaurant order management system that allows you to manage customers, restaurants, menu items, and orders. It consists of three main Python files: `seed.py`, `app.py`, and `management.py`.

## Table of Contents
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Commands](#commands)
- [License](#license)

## Project Structure

The project consists of the following Python files:

1. `seed.py`: This script is responsible for seeding initial data into the database, including customers, restaurants, menu items, and orders. It utilizes the SQLAlchemy ORM and the Faker library to generate mock data.

2. `app.py`: This file defines the data models and the database schema using SQLAlchemy. It also contains classes for `Customer`, `Restaurant`, `MenuItem`, `Order`, and `OrderedItem`. These classes define the structure of the database tables and their relationships.

3. `management.py`: This script provides a command-line interface (CLI) for managing customer orders. It allows you to view all data, search for customers, create new customers, add orders for customers, and delete orders.

## Getting Started

### Prerequisites

Before running the project, make sure you have the following prerequisites installed:

- Python 3.x
- SQLAlchemy
- Click
- Faker

You can install these dependencies using `pip`:

```bash
pip install SQLAlchemy Click Faker
```


### Installation

1. Clone the repository to your local machine or download the script files.

2. Navigate to the project directory:

    ```bash
    cd restaurant-order-management
    ```

## Usage
To use the Restaurant Order Management System, you can interact with it using the command-line interface provided by the management.py script.

### Running the CLI
You can run the CLI by executing the following command in your terminal:

```bash
python management.py [OPTIONS]
```

Replace [OPTIONS] with one of the available commands described below.

### Commands
- --view: View all data, including customers, restaurants, menu items, orders, and ordered items.

- --search <username>: Search for a specific customer by their username.

- --create-customer: Create a new customer.

- --add-order <username>: Add an order for a customer by specifying their username.

- --delete-order <order_id>: Delete an order for a customer by specifying its order ID.

### Example Usage
Here are some examples of how to use the CLI commands:


### Viewing all data:
```bash
python management.py --view
```

### Searching for a customer:
```bash
python management.py --search kristinawu
```

### Creating a new customer:
```bash
python management.py --create-customer
```

### Adding an order for a customer:
```bash
python management.py --add-order diana90
```

### Deleting an order for a customer:
```bash
python management.py --delete-order 1
```
### Viewing an order for a customer:
```bash
python3 management.py --view-orders megan28
```

## Contribution
Thank you for considering contributing to our project! We welcome contributions of all kinds, including bug reports, feature requests, documentation updates, and code contributions.

To contribute to the project, please follow these steps:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.


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

```c
You can create a `README.md` file in your project's repository and paste this content into it.
```
