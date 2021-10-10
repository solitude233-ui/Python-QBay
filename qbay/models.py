from qbay import app
from flask_sqlalchemy import SQLAlchemy


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

    def __repr__(self):
        return '<User %r>' % self.username


class transaction(db.Model):
    """Creates the transaction entities and attributes inside the data base."""
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120), unique=True, nullable=False)
    product_id = db.Column(db.Integer, unique=True, nullable=False)
    price = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.String(20), unique=True, nullable=False)


class product(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    lastModDate = db.Column(db.Date, nullable=False)
    ownerEmail = db.Column(
        db.String, db.ForeignKey('user.email'),
        nullable=False)


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
    if ((not product_title.isalnum()) or product_title[0] == " " or
            product_title[-1] == " "):
        print(
            "The title has to be alphanumeric only and "
            "the first and last character cannot be space.")

    if len(product_title) > 80:
        print("Length of the product title cannot exceed 80 characters")

    if (len(product_description) < 20 or len(product_description) > 2000):
        print(
            "Lenght of the product description should be at least "
            "20 characters and at most 2000 characters")

    if len(product_description) <= len(product_title):
        print("Length of description must be longer than the product's title.")

    if price < 10 or price > 10000:
        print("Price has to be within the range of [10,10000]")

    # Check if the date is within range
    dates = last_modified_date.split("-")
    if dates[0] >= "2021" and dates[0] <= "2025":
        if dates[0] == "2025":
            if dates[1] > "01":
                print("Date has to be after 2021-01-02 and before 2025-01-02.")
            elif dates[2] > "02":
                print("Date has to be after 2021-01-02 and before 2025-01-02.")
    else:
        print("Date has to be after 2021-01-02 and before 2025-01-02.")

    # Check if own email is empty
    if (len(owner_email) == 0):
        print("Owner email cannot be empty")

    # Check if the owner exists in the database
    exist_owner = User.query.filter_by(email=owner_email).first()
    if exist_owner is None:
        print("The user doesn't exist in the data base")

    # Check if the title already exists under the same user
    exist_title = product.query.filter_by(
        ownerEmail=owner_email, title=product_title)
    if exist_title is not None:
        print("The product title already exits under the same user.")

    # Add the product under the user database
    new_product = product(
        tile=product_title,
        description=product_description, price=price,
        lastModDate=last_modified_date, ownerEmail=owner_email)
    # add it to the current database session
    db.session.add(new_product)
    # actually save the user object
    db.session.commit()
