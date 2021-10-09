from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class product(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    lastModDate = db.Column(db.Date, nullable=False)
    ownerEmail = db.Column(db.String, db.ForeignKey('owner.email'),
                           nullable=False)

# Update product takes in the below self-explanatory parameters, then runs
# them through verifyInputs() to ensure they meet the specifications. If
# they do, then it updates the product record.


def updateProduct(ID, newID, title, description, price):
    productToUpdate = product.query.filter_by(ID=ID).first()
    if(verifyInputs(productToUpdate, newID, title, description, price) and
       date.today() > date(2021, 1, 2) and date.today < date(2025, 1, 2)):
        productToUpdate.ID = newID
        productToUpdate.title = title
        productToUpdate.description = description
        productToUpdate.price = price
        productToUpdate.lastModDate = date.today()

# Take in the parameters and check them for conformity with specifications


def verifyInputs(product, newID, title, description, price):
    oldPrice = product.price
    oldID = product.ID
# If title is not less than or equal to 80 chars, isnt alphanumeric +
# spaces (excluding prefix and suffix whitespace) then return false
    if (not(len(title) <= 80 and title.replace(' ', '').isalnum() and
        (title[:1] == ' ' or title[:1].isalnum()) and
        (title[len(title) - 1:len(title)] == ' ' or
         title[len(title) - 1:len(title)].isalnum()))):
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
            product.query.filter_by(ID=newID).first() is None)):
        return False
