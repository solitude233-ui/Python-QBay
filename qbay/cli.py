from qbay.models import login, register, create_product, updateProduct, \
    update_user_profile
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
    while not update:
        selection = input("Please enter 1 to update your user name, 2 to "
                          "update your shipping address, or 3 to update your "
                          "postal code: ")
        if selection == "1":
            new_user_name = "Enter your new user name: "
            if update_user_profile(user_email, new_user_name, "user name") \
                    is False:
                print("Failed to update user name.")
            else:
                print("User name updated successfully.")
        elif selection == "2":
            new_shipping_address = "Enter your new shipping address: "
            if update_user_profile(user_email, new_shipping_address,
                                   "shipping address") is False:
                print("Failed to update shipping address.")
            else:
                print("Shipping address updated successfully.")

        elif selection == "3":
            new_postal_code = "Enter your new postal code: "
            if update_user_profile(user_email, new_postal_code, "postal code")\
                    is False:
                print("Failed to updated postal code.")
            else:
                print("Postal code updated successfully.")

        end_update = "Would you like to continue updating your profile? " \
                     "Please enter 1 to update another item, or 2 to quit. "
        if end_update == "2":
            update = False

