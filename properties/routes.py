from flask import render_template, request, Blueprint, redirect, url_for, session
from models import db
from models.models import Properties, Clients, Users, MatchView
from flask_login import LoginManager, login_required
from properties.locations import hyderabad_locations

properties = Blueprint(
    "properties", __name__, template_folder="templates", static_folder="static"
)


def validate_data(data_dict):
    for key, value in data_dict.items():
        if value == "":
            data_dict[key] = None
        elif value.isdigit():
            data_dict[key] = int(value)
    return data_dict

@properties.route("/add-property", methods=["GET", "POST"])
@login_required
def add_properties():
    if request.method == "POST":
        property_data = dict(request.form)
        clean_data = validate_data(property_data)
        new_property = Properties(
            address1=clean_data["address1"],
            property_type=clean_data["property_type"],
            city=clean_data["city"],
            project_name=clean_data["project_name"],
            min_price=clean_data["min_price"],
            max_price=clean_data["max_price"],
            bedrooms=clean_data["bedrooms"],
            bathrooms=clean_data["bathrooms"],
            facing_direction=clean_data["facing_direction"],
            min_sqft=clean_data["min_sqft"],
            max_sqft=clean_data["max_sqft"],
            price_per_sqft=clean_data["price_per_sqft"],
            possession=clean_data["possession"],
            is_gated=clean_data["is_gated"],
            uds=clean_data["uds"],
            min_land_size=clean_data["min_land_size"],
            max_land_size=clean_data["max_land_size"],
            price_per_acre=clean_data["price_per_acre"],
            type_of_ownership=clean_data["type_of_ownership"],
            multiple_properties=clean_data["multiple_properties"],
            purpose=clean_data["purpose"],
            agent_name=session["agent_name"],
            agent_phone=session["agent_phone"],
            agent_role=clean_data["agent_role"],
            user_id=session["user_id"],
        )
        db.session.add(new_property)
        db.session.commit()
        return redirect("/property/dashboard-properties")
    return render_template("addproperty.html", locations = hyderabad_locations)


@properties.route("/add-client", methods=["GET", "POST"])
@login_required
def add_client():
    if request.method == "POST":
        client_data = dict(request.form)
        clean_data = validate_data(client_data)
        new_client = Properties(
            property_type=clean_data["property_type"],
            project_name=clean_data["project_name"],
            city=clean_data["city"],
            min_price=clean_data["min_price"],
            max_price=clean_data["max_price"],
            bedrooms=clean_data["bedrooms"],
            bathrooms=clean_data["bathrooms"],
            facing_direction=clean_data["facing_direction"],
            min_sqft=clean_data["min_sqft"],
            max_sqft=clean_data["max_sqft"],
            possession=clean_data["possession"],
            is_gated=clean_data["is_gated"],
            min_land_size=clean_data["min_land_size"],
            max_land_size=clean_data["max_land_size"],
            price_per_sqft=clean_data["price_per_sqft"],
            price_per_acre=clean_data["price_per_acre"],
            type_of_ownership=clean_data["type_of_ownership"],
            purpose=clean_data["purpose"],
            agent_name=session["agent_name"],
            agent_phone=session["agent_phone"],
            agent_role=clean_data["agent_role"],
            user_id=session["user_id"],
        )
        db.session.add(new_client)
        db.session.commit()
        return redirect("/property/dashboard-clients")
    return render_template("addclient.html")


@properties.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        property_type = request.form.get("property_type")
        # city = request.form.get("city")
        min_price = int(request.form.get("min_price"))
        max_price = int(request.form.get("max_price"))
        bathrooms = int(request.form.get("bathrooms"))
        bedrooms = int(request.form.get("bedrooms"))

        query = Properties.query
        
        if property_type:
            query = query.filter(Properties.property_type == property_type)
        if min_price:
            query = query.filter(Properties.min_price >= min_price)
        if max_price:  
            query = query.filter(Properties.max_price <= max_price) 
        if bedrooms:
                query = query.filter(Properties.bedrooms == bedrooms)
        if bathrooms:
                query = query.filter(Properties.bathrooms == bathrooms)
                      
        # Fetch results
        results = query.all()
        return render_template("search-results.html", results=results)


    return render_template("search.html")


@properties.route("/dashboard-properties", methods=["GET", "POST"])
@login_required
def dashboard():
    user_ID = session["user_id"]
    results = MatchView.query.filter_by(user_id=user_ID, agent_role='Seller').all()
    return render_template("dashboard-properties.html", results=results)

@properties.route("/dashboard-clients", methods=["GET", "POST"])
@login_required
def dashboard1():
    user_ID = session["user_id"]
    results = MatchView.query.filter_by(user_id=user_ID, agent_role='Buyer').all()
    return render_template("dashboard-clients.html", results=results)

@properties.route("/dashboard-test", methods=["GET", "POST"])
@login_required
def dashboard2():
    user_ID = session["user_id"]
    results = MatchView.query.filter_by(user_id=user_ID, agent_role='Seller').all()
    return render_template("test7.html", results=results)


@properties.route("/dashboard/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        Property_id = request.form.get("property_id")
        property_to_delete = Properties.query.get(Property_id)
        if property_to_delete:
            db.session.delete(property_to_delete)  # Delete the property
            db.session.commit()
            return redirect("/property/dashboard-properties")
    else:   
        return render_template("delete.html")


@properties.route("/dashboard/edit", methods=["GET", "POST"])
def edit_form():
        Property_id = request.form.get("property_id")
        record = Properties.query.filter_by(id=Property_id).first()
        if record.agent_role == "Seller": 
             return render_template("edit-properties.html", record=record)
        elif record.agent_role == "Buyer": 
            return render_template("edit-clients.html", record=record)

@properties.route("/dashboard/update", methods=["POST"])
def update():
    if request.method == "POST":
        Property_id = request.form.get("property_id")
        record = Properties.query.filter_by(id=Property_id).first()
        edit_data = dict(request.form)
        clean_data = validate_data(edit_data)
        record.address1 = clean_data["address1"]
        record.property_type = clean_data["property_type"]
        record.city = clean_data["city"]
        record.project_name = clean_data["project_name"]
        record.min_price = clean_data["min_price"]
        record.max_price = clean_data["max_price"]
        record.bedrooms = clean_data["bedrooms"]
        record.bathrooms = clean_data["bathrooms"]
        record.facing_direction = clean_data["facing_direction"]
        record.min_sqft = clean_data["min_sqft"]
        record.max_sqft = clean_data["max_sqft"]
        record.price_per_sqft = clean_data["price_per_sqft"]
        record.possession = clean_data["possession"]
        record.is_gated = clean_data["is_gated"]
        record.uds = clean_data["uds"]
        record.min_land_size = clean_data["min_land_size"]
        record.max_land_size = clean_data["max_land_size"]
        record.price_per_acre = clean_data["price_per_acre"]
        record.type_of_ownership = clean_data["type_of_ownership"]
        record.multiple_properties = clean_data["multiple_properties"]
        record.purpose = clean_data["purpose"]
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return f"Database update error: {e}", 500 
        return redirect("/property/dashboard-properties")
   
@properties.route("/dashboard/fetch", methods=["POST"])
def fetch():
    if request.method == "POST":
        Property_id = request.form.get("property_id")
        current_property = Properties.query.filter_by(id=Property_id).first()
        property_type = current_property.property_type
        min_price = current_property.min_price 
        max_price = current_property.max_price 
        min_sqft = current_property.min_sqft
        max_sqft = current_property.max_sqft
        bedrooms = current_property.bedrooms
        bathrooms = current_property.bathrooms
        min_land_size = current_property.min_land_size
        max_land_size = current_property.max_land_size
        agent_role = current_property.agent_role

        query = Properties.query.filter(
        Properties.id != Property_id,
        Properties.property_type == property_type,
        Properties.min_price <= max_price,
        Properties.max_price >= min_price,
        Properties.agent_role != agent_role
        )
        if property_type in ["Apartment", "Villa"]:
            query = query.filter(
                Properties.bedrooms == bedrooms,
                Properties.bathrooms == bathrooms
            )
        elif property_type in ["Plot", "Commercial"]:
            query = query.filter(
            Properties.min_sqft <= max_sqft,
            Properties.max_sqft >= min_sqft
            )
        elif property_type == "Land":
            query = query.filter(
            Properties.min_land_size <= max_land_size,
            Properties.max_land_size >= min_land_size
            )
        matching_properties = query.all()
        return render_template("match.html", results = matching_properties)

@properties.route("/test")
def test8():
    return render_template("test8.html")

