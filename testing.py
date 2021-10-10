import random

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URsI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


def test_update_user_profile():
    # Correct variables to test
    user_email = "John.Smith@gmail.com"
    user_name = "John"
    shipping_address = "220 Yonge Street"
    postal_code = "M5B 2H1"
    value_to_update = None

    print("-------------- Testing Begins --------------")

    # Testing invalid user name inputs
    # Test incorrect value: user name is empty
    test1_user_name = ""
    print("Testing an empty user name: ")
    update_user_profile(user_email, test1_user_name, shipping_address, postal_code, value_to_update)

    # Test incorrect value: user name has special character
    test2_user_name = "Jo!hn"
    print("Testing a user name with special character: ")
    update_user_profile(user_email, test2_user_name, shipping_address, postal_code, value_to_update)

    # Test incorrect value: user name has space as prefix
    test3_user_name = " John"
    print("Testing a user name with a space: ")
    update_user_profile(user_email, test3_user_name, shipping_address, postal_code, value_to_update)

    # Test incorrect value: user name is too short
    test4_user_name = "J"
    print("Testing a user name too short: ")
    update_user_profile(user_email, test4_user_name, shipping_address, postal_code, value_to_update)

    # Test incorrect value: user name is too long
    test5_user_name = "John Smith John Smith John Smith"
    print("Testing a user name too long: ")
    update_user_profile(user_email, test5_user_name, shipping_address, postal_code, value_to_update)

    # Testing invalid shipping address inputs
    # Test incorrect value: shipping address is empty
    test1_shipping_address = ""
    print("Testing an empty shipping address: ")
    update_user_profile(user_email, user_name, test1_shipping_address, postal_code, value_to_update)

    # Test incorrect value: shipping address has special characters
    test2_shipping_address = "220 Yo!nge Street"
    print("Testing a shipping address with special characters: ")
    update_user_profile(user_email, user_name, test2_shipping_address, postal_code, value_to_update)

    # Testing invalid postal code inputs
    # Test incorrect value: invalid postal code
    test1_postal_code = "M5B 2!1"
    print("Testing an invalid postal code: ")
    update_user_profile(user_email, user_name, shipping_address, test1_postal_code, value_to_update)

    print("-------------- Testing Completed --------------")


def test_login():
    # Correct variables to test
    user_email = "John.Smith@gmail.com"
    user_password = "Password!"
    address = "@gmail.com"

    print("-------------- Testing Begins --------------")

    # Testing invalid user email inputs
    # Test incorrect value: user email is empty
    test1_user_email = ""
    print("Testing an empty user email: ")
    login(test1_user_email, user_password)

    # Test incorrect value: user email local part it too long
    aLetter = "j"
    local_part = ''.join(random.choice(aLetter) for i in range(65))
    test2_user_email = aLetter + address
    print("Testing a user email with a long local part: ")
    login(test2_user_email, user_password)

    # Test incorrect value: user email domain is too long
    aLetter = "j"
    domain = ''.join(random.choice(aLetter) for i in range(256))
    test3_user_email = aLetter + address + domain
    print("Testing a user email with a long domain: ")
    login(test3_user_email, user_password)

    # Test incorrect value: user email starts with a period
    test4_user_email = ".John.Smith@gmail.com"
    print("Testing a user email that starts with a period: ")
    login(test4_user_email, user_password)

    # Test incorrect value: user email ends with a hyphen
    test5_user_email = "John.Smith@gmail.com-"
    print("Testing a user email that ends with a hyphen: ")
    login(test5_user_email, user_password)

    # Test incorrect value: user password is empty
    test1_user_password = ""
    print("Testing a user password that is empty: ")
    login(user_email, test1_user_password)

    # Test incorrect value: user password is too short
    test2_user_password = "P"
    print("Testing a user password that is too short: ")
    login(user_email, test2_user_password)

    # Test incorrect value: user password does not have a capitalized letter
    test3_user_password = "password!"
    print("Testing a user password that does not have a capitalized letter: ")
    login(user_email, test3_user_password)

    # Test incorrect value: user password does not have a lowercase letter
    test4_user_password = "PASSWORD!"
    print("Testing a user password that does not have a lowercase letter: ")
    login(user_email, test4_user_password)

    # Test incorrect value: user password does not have a special character
    test5_user_password = "Password"
    print("Testing a user password that does not have a special character: ")
    login(user_email, test5_user_password)
