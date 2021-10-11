import re
import string
from qbay import app
from flask_sqlalchemy import SQLAlchemy
from datetime import date

'''
This file defines data models and related business logics
'''

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False,
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)
    products = db.relationship('product', backref="user", lazy=True)

    def __repr__(self):
        return '<User %r>' % self.username


class Transaction(db.Model):
    """Creates the transaction entities and attributes inside the database."""
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.String(20), unique=True, nullable=False)


class Product(db.Model):
    """Creates the product entity and related attributes in the database."""
    ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    lastModDate = db.Column(db.Date, nullable=False)
    ownerEmail = db.Column(db.String, db.ForeignKey('user.email'),
                           nullable=False)


class Review(db.Model):
    """Initializes the Review class."""
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(80), unique=True, nullable=False)
    score = db.Column(db.String(120), unique=True, nullable=False)
    review = db.Column(db.String(400), unique=True, nullable=False)


# create all tables
db.create_all()


def register(name, email, password):
    '''
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    '''
    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
    # add it to the current database session
    db.session.add(user)
    # actually save the user object
    db.session.commit()

    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]


def create_product(product_title, product_description, price,
                   last_modified_date, owner_email):
    """Creates a product under a user.
    Check if all the attributes being created are valid before creating 
    the product in the database."""
    # Test if the title is correct
    if product_title[0] == " " or product_title[-1] == " " or (
            not product_title.replace(" ", "").isalnum()):
        print("The title has to be alphanumeric only and the "
              "first and last character cannot be space.")
        return None

    if len(product_title) > 80:
        return None
        print("Length of the product title cannot exceed 80 characters")

    if (len(product_description) < 20 or len(product_description) > 2000):
        return None
        print("Lenght of the product description should be at least "
              "20 characters and at most 2000 characters")

    if len(product_description) <= len(product_title):
        return None
        print("Length of description must be longer than the product's title.")

    if price < 10 or price > 10000:
        print("Price has to be within the range of [10,10000].")
        return None

    # Check if the date is within range
    if last_modified_date < date(
            2021, 1, 2) or last_modified_date > date(
            2025, 1, 2):
        print("Date has to be between 2021-01-02 and 2025-01-02.")
        return None

    # Check if own email is empty
    if (len(owner_email) == 0):
        print("Owner email cannot be empty.")
        return None

    # Check if the owner exists in the database
    exist_owner = User.query.filter_by(email=owner_email).first()
    if exist_owner is None:
        print("The user doesn't exist in the data base.")
        return None

    # Check if the title already exists under the same user
    exist_title = product.query.filter_by(
        ownerEmail=owner_email, title=product_title)
    if exist_title is not None:
        print("The product title already exits under the same user.")
        return None

    # Add the product under the user database
    new_product = product(
        title=product_title,
        description=product_description, price=price,
        lastModDate=last_modified_date, ownerEmail=owner_email)
    # add it to the current database session
    db.session.add(new_product)
    # actually save the product object
    db.session.commit()

    return True

  
def updateProduct(ID, newID, title, description, price, ownerEmail):
    productToUpdate = product.query.filter_by(ID=ID,
                                              ownerEmail=ownerEmail).first()
    if(verifyProductInputs(productToUpdate, newID, title, description, price)
            and date.today() > date(2021, 1, 2) and 
            date.today < date(2025, 1, 2)):
        productToUpdate.ID = newID
        productToUpdate.title = title
        productToUpdate.description = description
        productToUpdate.price = price
        productToUpdate.lastModDate = date.today()
        return True
    else:
        return False
# Take in the parameters and check them for conformity with specifications


def verifyProductInputs(product, newID, title, description, price):
    oldPrice = product.price
    oldID = product.ID
# If title is not less than or equal to 80 chars, isnt alphanumeric +
# spaces (excluding prefix and suffix whitespace) then return false
    if (not(len(title) <= 80 and title.replace(' ', '').isalnum() and
        (title[:1] == ' ' or title[:1].isalnum()) and
        (title[len(title) - 1:len(title)] == ' ' or
         title[len(title) - 1:len(title)].isalnum()))):
        return False
    # Check that the title isn't already in use
    if (product.query.filter_by(title=title).all() > 0):
        return False
    
        # If the description is not greater than or equal to 20 chars, less
        # than or equal to 2000 chars, and is not longer than title, return
        # false
    if (not(len(description) >= 20 and len(description)
            <= 2000 and len(description) > len(title))):
        return False
        # Price must be greater and fall in the bounds of 10 to 10,000
        # inclusive
    if (not(price > oldPrice and price >= 10 and price <= 10000)):
        return False
        # The new ID must not already be in use
    if (not(newID == oldID or
            product.query.filter_by(ID=newID,
                                    ownerEmail=product.ownerEmail).first()
            is None)):
        return False
    return True

  
def update_user_profile(user_email, user_name, shipping_address,
                        postal_code, value_to_update):
    
    special = [
        "!", "#", "$", 
        "%", "&", "'", 
        "*", "+", "-", 
        "/", "=", "?", 
        "^", "_", "`", 
        "{", "|", "}",
        "~"]

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
        None
        # if value_to_update.lower() == "shipping address":
        # user.shipping_address = shipping_address
        # return True

    # Check validity of postal_code
    regex = "[ABCEGHJKLMNPRSTVXY][0-9][ABCEGHJKLMNPRSTVWXYZ]"\
            " ?[0-9][ABCEGHJKLMNPRSTVWXYZ][0-9]"
    if re.match(regex, postal_code) is None:
        print("Error: Invalid postal code")
        return False
    else:
        None
        # if value_to_update.lower() == "postal code)":
        # user.postal_code = postal_code
        # return True

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
        None
        # if value_to_update.lower() == "user name":
        # user.user_name = user_name
        # return True


def login(user_email, user_password):
    special = [
        "!", "#", "$", 
        "%", "&", "'",
        "*", "+", "-",
        "/", "=", "?",
        "^", "_", "`",
        "{", "|", "}",
        "~"]

    local_part = user_email.split("@")[0]

    # CHECK EMAIL
    # Check validity of email for case: local part does not start/end 
    # with quotes
    if not local_part.startswith('"') or not local_part.endswith('"'):
        # Check email is empty
        if len(user_email) == 0:
            print("Error: Email cannot be empty.")
            return False
        # Check if email is too long
        elif len(user_email.split("@")[0]) > 64:
            print("Error: Email is too long.")
            return False
        # Check if email is too long
        elif len(user_email.split("@")[1]) > 255:
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
        if (
            len(user_email.split("@")[0]) > 64
            or len(user_email.split("@")[1]) > 255
        ):
            print("Error: Email is too long.")
            return False

    # CHECK PASSWORD
    # Check if password is empty
    if user_password == "":
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
