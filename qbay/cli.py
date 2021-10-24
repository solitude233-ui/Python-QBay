from qbay.models import login, register, create_product, updateProduct, product
from datetime import date


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def register_page():
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
    """
    This is the page that allows the user to create a product.
    It prompts the user to enter all the required information and call the
    create_product function to attempt to create a new product."""
    title = input("Please enter the title of your product: ")
    description = input("Please enter the description of your product: ")
    price = float(input("Please enter the price of your product: "))
    year = int(input("Please enter the last modified year: "))
    month = int(input("Please enter the last modified month: "))
    day = int(input("Please enter the last modified day: "))
    date1 = date(year, month, day)
    email = input("Please enter your email: ")

    if create_product(title, description, price, date1, email) is None:
        print("Failed to create a product.")
    else:
        print("Product created successfully!")


def update_product_page():
    """
    The function allows the user to update the parameters of a specific
    product. It asks the user to input their email and ID of the
    product, and the updated parameters for the product.
    Then it checks if the produxt exists. If it does
    Then the method simply tries to update the product by calling
    a pre-existing update_product() function.
    It prints a message to let the user know if it was succesful.
    """
    # Ask user for the required inputs
    email = input(
        "Enter the email of the user who's product you'd like to update: ")
    ID = int(input(
        "Please input the ID of the product you'd like to update: "))
    newID = int(input("Enter the updated ID of the product: "))
    title = (input("Enter an updated Title: "))
    description = (input("Enter an updated description of the product: "))
    price = float(input("Enter an updated price of the product: "))
    # Check if the prodcut actually exists
    if(product.query.filter_by(ownerEmail=email, title=title).first() is None):
        print("Failure. The product doesn't exist under the user. Try again")
        return
    # If the product exists, try to update it
    if(updateProduct(ID, newID, title, description, price, email)):
        print("Successs")
    else:
        print("Failure. Check your inputs follow specifications and try again")
