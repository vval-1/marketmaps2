from flask_sqlalchemy import SQLAlchemy
from . import db

class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key = True)
    address1 = db.Column(db.String(100), nullable=False)
    address2 = db.Column(db.String(100), nullable=True)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    zipcode = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Float, nullable=False)
    bathrooms = db.Column(db.Float, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    
    def __init__(self, address1, city, state, zipcode, price, bedrooms, bathrooms, address2=None, comments=None):
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.comments = comments

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    userID = db.Column(db.Float, nullable=False)

    def __init__(self, email, username, password, userID):
        self.email = email
        self.username = username
        self.password = password
        self.userID = userID

class Clients(db.Model):
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key = True)
    contact = db.Column(db.String, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Float, nullable=False)
    bathrooms = db.Column(db.Float, nullable=False)
    comments = db.Column(db.Text, nullable=True) 

    def __init__(self, contact, city, state, price, bedrooms, bathrooms, comments=None):
        self.contact = contact
        self.city = city
        self.state = state
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.comments = comments