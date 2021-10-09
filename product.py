from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class product(db.Model):
    productID = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float,nullable=False)
    lastModDate = db.Column(db.Date,nullable=False)
    ownerEmail = db.Column(db.String, db.ForeignKey(owner.email), nullable=False)

def updateProduct():
    pass

def verifyInputs():
    pass