import re

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


def update_user_profile(user_email, user_name, shipping_address, postal_code, value_to_update):
    special = ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~"]
    user = User.query.filter_by(email=user_email).first()

    # Check validity of shipping address
    if len(shipping_address) == 0:
        print("Error: Shipping address cannot be empty.")
        return False
    elif not (shipping_address.replace(' ', '')).isalnum():
        print("Error: Shipping address should be alphanumeric-only.")
        return False
    elif any(x in shipping_address for x in special):
        print("Error: Shipping address cannot contain special characters.")
        return False
    else:
        if value_to_update.lower() == "shipping address":
            user.shipping_address = shipping_address
            return True

    # Check validity of postal_code
    regex = "[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ] ?[0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]"
    if re.match(regex, postal_code) is None:
        print("Error: Invalid postal code")
        return False
    else:
        if value_to_update.lower() == "postal code)":
            user.postal_code = postal_code
            return True

    # Check validity of user_name
    if len(user_name) == 0:
        print('Error: User name cannot be empty.')
        return False
    elif not (user_name.replace(' ', '')).isalnum():
        print("Error: User name must be alphanumeric-only.")
        return False
    elif user_name.startswith(" ") or user_name.endswith(" "):
        print("Error: User name cannot start or end with a space.")
        return False
    elif len(user_name) < 3:
        print("Error: User name must be greater than 2 characters.")
        return False
    elif len(user_name) > 20:
        print("Error: User name must be less than 20 characters.")
        return False
    else:
        if value_to_update.lower() == "user name":
            user.user_name = user_name
            return True


def login(user_email, user_password):
    special = ["!", "#", "$", "%", "&", "'", "*", "+", "-", "/", "=", "?", "^", "_", "`", "{", "|", "}", "~"]
    local_part = user_email.split("@")[0]

    # CHECK EMAIL
    # Check validity of email for case: local part does not start/end with quotes
    if not local_part.startswith('"') or not local_part.endswith('"'):
        # Check email is empty
        if len(user_email) == 0:
            print("Error: Email cannot be empty.")
            return False
        # Check if email is too long
        elif len(user_email.split("@")[0]) > 64 or len(user_email.split("@")[1]) > 255:
            print("Error: Email is too long.")
            return False
        # Check if email starts or ends with period
        elif user_email.startswith(".") or user_email.endswith("."):
            print("Error: Email cannot start or end with a period.")
            return False
        # Check if email starts or ends with a hyphen
        elif user_email.startswith("-") or user_email.endswith("-"):
            print("Error: Email cannot start or end with a hyphen.")
            return False
        # Check if email contains consecutive periods
        for i in range(len(user_email) - 2):
            if user_email[i:i + 2] == "..":
                print("Error: Email cannot contain consecutive periods.")
                return False

    # Check validity of email for case: local part starts/ends with quotes
    else:
        # Check email length
        if len(user_email.split("@")[0]) > 64 or len(user_email.split("@")[1]) > 255:  # CHECK IF THIS IS OCTETS
            print("Error: Email is too long.")
            return False

    # CHECK PASSWORD
    # Check if password is empty
    if len(user_password) == 0:
        print("Error: Password cannot be empty.")
        return False
    # Check if password length is too short
    elif len(user_password) < 6:
        print("Error: Password must be at least 6 characters.")
        return False
    # Check if password contains at least one uppercase character
    elif not (any(x.isupper() for x in user_password)):
        print("Error: Password must have at least one uppercase character.")
        return False
    # Check if password contains at least one lowercase character
    elif not (any(x.islower() for x in user_password)):
        print("Error: Password must have at least one lowercase character.")
        return False
    # Check if password contains at least one special character
    elif not any(x in user_password for x in special):
        print("Error: Password must have at least one special character.")
        return False

    # Check if user exists in the database
    valid = False
    user = User.query.filter_by(email=user_email).first()
    while not valid:
        if user_email != user.user_email:
            print("Invalid username.")
            user_email = input("Please enter email: ")
        else:
            if user_password != user.user_password:
                print("Invalid password.")
                user_email = input("Please enter email: ")
                user_password = input("Please enter password: ")
            else:
                valid = True
