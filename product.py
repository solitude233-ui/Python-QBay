from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class product(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float,nullable=False)
    lastModDate = db.Column(db.Date,nullable=False)
    ownerEmail = db.Column(db.String, db.ForeignKey(owner.email), nullable=False)

def updateProduct(ID, newID, title, description, price):
    productToUpdate = product.query.filter_by(ID=ID).first()
    if(verifyInputs(productToUpdate, newID, title, description, price) and date.today()>date(2021, 1, 2) and date.today<date(2025, 1, 2) ):
        productToUpdate.ID = newID
        productToUpdate.title = title
        productToUpdate.description = description
        productToUpdate.price = price
        productToUpdate.lastModDate = date.today()

def verifyInputs(product, newID, title, description, price):
    oldPrice = product.price
    oldID = product.ID

    if(not(len(title)<=80 and title.replace(' ','').isalnum() and (title[:1]==' ' or title[:1].isalnum()) and (title[len(title)-1:len(title)]==' ' or title[len(title)-1:len(title)].isalnum()))):
        return False
    if (not(len(description)>=20 and len(description)<=2000 and len(description)>len(title))):
        return False
    if (not(price>oldPrice and price>=10 and price<=10000)):
        return False
    if (not(newID==oldID or product.query.filter_by(ID=newID).first() is None):
        return False