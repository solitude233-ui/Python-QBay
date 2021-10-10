from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Review(db.Model):
    """Initializes the Review class.

    """
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(80), unique=True, nullable=False)
    score = db.Column(db.String(120), unique=True, nullable=False)
    review = db.Column(db.String(400), unique=True, nullable=False)
