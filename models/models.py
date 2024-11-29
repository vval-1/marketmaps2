from flask_sqlalchemy import SQLAlchemy
from . import db
from flask_login import UserMixin


class Properties(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(100), nullable=True)
    property_type = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(30), nullable=True)
    min_price = db.Column(db.Float, nullable=True)
    max_price = db.Column(db.Float, nullable=True)
    bedrooms = db.Column(db.Float, nullable=True)
    bathrooms = db.Column(db.Float, nullable=True)
    facing_direction = db.Column(db.String(10), nullable=True)
    min_sqft = db.Column(db.Float, nullable=True)
    max_sqft = db.Column(db.Float, nullable=True)
    possession = db.Column(db.String(30), nullable=True)
    is_gated = db.Column(db.String(10), nullable=True)
    uds = db.Column(db.Float, nullable=True)
    plot_size = db.Column(db.Float, nullable=True)
    land_size = db.Column(db.Float, nullable=True)
    price_per_acre = db.Column(db.Float, nullable=True)
    type_of_ownership = db.Column(db.String(30), nullable=True)
    purpose = db.Column(db.String(30), nullable=True)
    agent_name = db.Column(db.String(30), nullable=True)
    agent_phone = db.Column(db.Float, nullable=True)
    comments = db.Column(db.Text, nullable=True)
    agent_role = db.Column(db.String(30), nullable=True)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(
        self,
        address1=None,
        property_type=None,
        city=None,
        min_price=None,
        max_price=None,
        bedrooms=None,
        bathrooms=None,
        facing_direction=None,
        possession=None,
        is_gated=None,
        uds=None,
        plot_size=None,
        land_size=None,
        price_per_acre=None,
        type_of_ownership=None,
        purpose=None,
        agent_name=None,
        agent_phone=None,
        agent_role=None,
        user_id=None,
        comments=None,
    ):
        self.address1 = address1
        self.property_type = property_type
        self.city = city
        self.min_price = min_price
        self.max_price = max_price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.facing_direction = facing_direction
        self.possession = possession
        self.is_gated = is_gated
        self.uds = uds
        self.plot_size = plot_size
        self.land_size = land_size
        self.price_per_acre = price_per_acre
        self.type_of_ownership = type_of_ownership
        self.purpose = purpose
        self.agent_name = agent_name
        self.agent_phone = agent_phone
        self.agent_role = agent_role
        self.user_id = user_id
        self.comments = comments


class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


class Clients(db.Model):
    __tablename__ = "clients"

    id = db.Column(db.Integer, primary_key=True)
    contact = db.Column(db.String, nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Float, nullable=False)
    bedrooms = db.Column(db.Float, nullable=False)
    bathrooms = db.Column(db.Float, nullable=False)
    comments = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, nullable=False)

    def __init__(
        self, contact, city, state, price, bedrooms, bathrooms, user_id, comments=None
    ):
        self.contact = contact
        self.city = city
        self.state = state
        self.price = price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.comments = comments
        self.user_id = user_id
