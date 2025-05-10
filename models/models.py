from . import db
from flask_login import UserMixin
import datetime


class Properties(db.Model):
    __tablename__ = "properties"

    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(100), nullable=True)
    project_name = db.Column(db.String(100), nullable=True)
    property_type = db.Column(db.String(20), nullable=True)
    city = db.Column(db.String(30), nullable=True)
    price = db.Column(db.Float, nullable=True)
    # max_price = db.Column(db.Float, nullable=True)
    bedrooms = db.Column(db.Float, nullable=True)
    bathrooms = db.Column(db.Float, nullable=True)
    facing_direction = db.Column(db.String(10), nullable=True)
    possession = db.Column(db.String(30), nullable=True)
    sqft = db.Column(db.Float, nullable=True)
    # max_sqft = db.Column(db.Float, nullable=True)
    price_per_sqft = db.Column(db.Float, nullable=True)
    is_gated = db.Column(db.String(10), nullable=True)
    uds = db.Column(db.Float, nullable=True)
    land_size = db.Column(db.Float, nullable=True)
    # max_land_size = db.Column(db.Float, nullable=True)
    plot_size = db.Column(db.Float, nullable=True)
    # max_plot_size = db.Column(db.Float, nullable=True)
    price_per_acre = db.Column(db.Float, nullable=True)
    price_per_sqyd = db.Column(db.Float, nullable=True)
    type_of_ownership = db.Column(db.String(30), nullable=True)
    multiple_properties = db.Column(db.String(10), nullable=True)
    purpose = db.Column(db.String(30), nullable=True)
    agent_name = db.Column(db.String(30), nullable=True)
    agent_phone = db.Column(db.Float, nullable=True)
    agent_role = db.Column(db.String(30), nullable=True)
    location = db.Column(db.String(100), nullable=True)
    user_id = db.Column(db.Integer, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=True)

    def __init__(
        self,
        address1=None,
        project_name = None,
        property_type=None,
        city=None,
        price=None,
        # max_price=None,
        bedrooms=None,
        bathrooms=None,
        facing_direction=None,
        possession=None,
        sqft=None,
        # max_sqft=None,
        price_per_sqft=None,
        is_gated=None,
        uds=None,
        land_size=None,
        # max_land_size=None,
        plot_size=None,
        # max_plot_size=None,
        price_per_acre=None,
        price_per_sqyd=None,
        type_of_ownership=None,
        multiple_properties=None,
        purpose=None,
        agent_name=None,
        agent_phone=None,
        agent_role=None,
        location=None,
        user_id=None,
        date_added=None,
    ):
        self.address1 = address1
        self.project_name = project_name
        self.property_type = property_type
        self.city = city
        self.price = price
        # self.max_price = max_price
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.facing_direction = facing_direction
        self.possession = possession
        self.sqft = sqft
        # self.max_sqft = max_sqft
        self.price_per_sqft = price_per_sqft
        self.is_gated = is_gated
        self.uds = uds
        self.land_size = land_size
        # self.max_land_size = max_land_size
        self.plot_size = plot_size
        # self.max_plot_size = max_plot_size
        self.price_per_acre = price_per_acre
        self.price_per_sqyd = price_per_sqyd
        self.type_of_ownership = type_of_ownership
        self.multiple_properties = multiple_properties
        self.purpose = purpose
        self.agent_name = agent_name
        self.agent_phone = agent_phone
        self.agent_role = agent_role
        self.location = location
        self.user_id = user_id
        self.date_added = date_added

class Users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)
    agent_name = db.Column(db.String(40), nullable=True)
    agent_phone = db.Column(db.BigInteger, nullable=True)
    date_added = db.Column(db.DateTime, default=datetime.datetime.now(), nullable=True)

    def __init__(self, email, password, agent_name=None, agent_phone=None, date_added=None):
        self.email = email
        self.password = password
        self.agent_name = agent_name
        self.agent_phone = agent_phone
        self.date_added = date_added


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


class MatchView(db.Model):
    __tablename__ = "match_view"
    __table_args__ = {"extend_existing": True}

    id = db.Column(db.BigInteger, primary_key=True)  # Assuming 'id' is a primary key
    property_type = db.Column(db.VARCHAR(20), nullable=True)
    location = db.Column(db.VARCHAR(100), nullable=True)
    project_name = db.Column(db.VARCHAR(100), nullable=True)
    min_price = db.Column(db.Float, nullable=True)
    max_price = db.Column(db.Float, nullable=True)
    bedrooms = db.Column(db.Float, nullable=True)
    min_sqft = db.Column(db.Float, nullable=True)
    min_land_size = db.Column(db.Float, nullable=True)
    min_plot_size = db.Column(db.Float, nullable=True)
    purpose = db.Column(db.String, nullable=True)
    agent_role = db.Column(db.String, nullable=True)
    user_id = db.Column(db.Integer, nullable=True)  # Assuming a users table exists
    match_count = db.Column(db.BigInteger, nullable=True)
