from qbay.models import login, register, create_product, updateProduct
from datetime import date


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def regsiter_page():
    email = input('Please input email:')
    password = input('Please input password:')
    password_twice = input('Please input the password again:')
    if password != password_twice:
        print('password entered not the same')
    elif register('default name', email, password):
        print('registration succceeded')
    else:
        print('regisration failed.')


def create_product_page():
    title = input("Please enter the title of your product: ")
    description = input("Please enter the description of your product: ")
    price = float(input("Please enter the price of your product: "))
    modified_date = date(
        input("Please enter the last modified date in "
              "(year, month, day) format: "))
    email = input("Please enter your email: ")

    if create_product(title, description, price, modified_date, email) is None:
        print("Failed to create a product.")
    else:
        print("Product created successfully!")
