from flask_sqlalchemy import SQLAlchemy
from . import db
from flask_login import UserMixin

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
    user_id = db.Column(db.Integer, nullable = False )
    
    def __init__(self, address1, city, state, zipcode, price, bedrooms, bathrooms, user_id, address2=None, comments=None):
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.comments = comments
        self.user_id = user_id

class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True) 
    email = db.Column(db.String(100), nullable=False, unique = True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

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
    user_id = db.Column(db.Integer, nullable = False )

    def __init__(self, contact, city, state, price, bedrooms, bathrooms, user_id,comments=None):
        self.contact = contact
        self.city = city
        self.state = state
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.comments = comments
        self.user_id = user_id