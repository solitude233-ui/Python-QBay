from qbay.models import login, register, create_product, updateProduct, \
    update_user_profile, product
from datetime import date


def login_page():
    '''
    Takes email and password information from the user and displays the
    result of the attempted login
    '''
    email = input('Please input email: ')
    password = input('Please input password: ')
    loginAttempt = login(email, password)
    if loginAttempt is False:
        print("Login failed")
    else:
        print("Login Sucessful")
        return loginAttempt


def register_page():
    '''
    Takes the user's email, username and password and attempts to register
    them as a new user. The function then displays the result of this
    registration attempt to the user.
    '''
    email = input("Please input your email: ")
    username = input("Please enter the username you would like to use: ")
    password = input("Please input password: ")
    password_twice = input("Please input the password again: ")
    if password != password_twice:
        print('password entered not the same: ')
    elif register(username, email, password):
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
    oldTitle = input("Enter the current title of the product: ")
    if(product.query.filter_by(ownerEmail=email, title=oldTitle).first()
       is None):
        print("Failure. The product doesn't exist under the user. Try again")
        return
    newID = int(input("Enter the updated ID of the product: "))
    title = (input("Enter an updated Title: "))
    description = (input("Enter an updated description of the product: "))
    price = float(input("Enter an updated price of the product: "))
    # Check if the prodcut actually exists

    # If the product exists, try to update it
    if(updateProduct(
       product.query.filter_by(ownerEmail=email, title=oldTitle).first().ID,
       newID, title, description, price, email)):
        print("Successs")
    else:
        print("Failure. Check your inputs follow specifications and try again")


def update_profile_page():
    """
    This page allows a user to update their user information, including their
    user name, email address, and postal code. The function prompts the user
    for their email address and which entity they would like to update. The
    function calls update_user_profile and returns false if the entity failed
    to be updated. The loop continues to prompt the user if they would like to
    continue updating their profile, or if they are finished and would like to
    quit.
    """
    user_email = input("Please enter your current log in email address: ")
    update = True
    while update:
        selection = input("Please enter 1 to update your user name, 2 to "
                          "update your shipping address, or 3 to update your "
                          "postal code: ")
        if selection == "1":
            new_user_name = input("Enter your new user name: ")
            if update_user_profile(user_email, new_user_name, "user name") \
                    is False:
                print("Failed to update user name.")
            else:
                print("User name updated successfully.")
                
        elif selection == "2":
            new_shipping_address = input("Enter your new shipping address: ")
            if update_user_profile(user_email, new_shipping_address,
                                   "shipping address") is False:
                print("Failed to update shipping address.")
            else:
                print("Shipping address updated successfully.")

        elif selection == "3":
            new_postal_code = input("Enter your new postal code: ")
            if update_user_profile(user_email, new_postal_code, "postal code")\
                    is False:
                print("Failed to updated postal code.")
            else:
                print("Postal code updated successfully.")
                
        end_update = input("Would you like to continue updating your profile? "
                           "Enter 1 to update another item, or 2 to quit.")

        if end_update == "2":
            update = False
