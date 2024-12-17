from flask import render_template, request, Blueprint, redirect, url_for, session
from models import db
from models.models import Properties, Clients, Users, MatchView
from flask_login import LoginManager, login_required

properties = Blueprint(
    "properties", __name__, template_folder="templates", static_folder="static"
)


def validate_data(data_dict):
    for key, value in data_dict.items():
        if value == "":
            data_dict[key] = None
        elif value.isdigit():
            data_dict[key] = float(value)
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
            min_price=clean_data["min_price"],
            max_price=clean_data["max_price"],
            bedrooms=clean_data["bedrooms"],
            bathrooms=clean_data["bathrooms"],
            facing_direction=clean_data["facing_direction"],
            min_sqft=clean_data["min_sqft"],
            max_sqft=clean_data["max_sqft"],
            possession=clean_data["possession"],
            is_gated=clean_data["is_gated"],
            uds=clean_data["uds"],
            plot_size=clean_data["plot_size"],
            land_size=clean_data["land_size"],
            price_per_acre=clean_data["price_per_acre"],
            type_of_ownership=clean_data["type_of_ownership"],
            purpose=clean_data["purpose"],
            agent_name=clean_data["agent_name"],
            agent_phone=clean_data["agent_phone"],
            agent_role=clean_data["agent_role"],
            user_id=session["user_id"],
        )
        db.session.add(new_property)
        db.session.commit()
        return render_template("search.html")
    return render_template("addproperty.html")


@properties.route("/add-client", methods=["GET", "POST"])
@login_required
def add_client():
    if request.method == "POST":
        contact = request.form.get("contact")
        city = request.form.get("city")
        state = request.form.get("state")
        price = float(request.form.get("price"))
        bedrooms = float(request.form.get("bedrooms"))
        bathrooms = float(request.form.get("bathrooms"))
        comments = request.form.get("comments")

        new_client = Clients(
            contact=contact,
            city=city,
            state=state,
            price=price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            comments=comments,
            user_id=session["user_id"],
        )

        db.session.add(new_client)
        db.session.commit()
        return redirect(render_template("search.html"))
    return render_template("addclient.html")


@properties.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        city = request.form.get("city")
        zipcode = request.form.get("zipcode")
        price = request.form.get("price")
        bedrooms = request.form.get("bedrooms")
        bathrooms = request.form.get("bathrooms")
        results = Properties.query.all()
        return render_template("search.html", results=results)

    return render_template("search.html")


@properties.route("/dashboard", methods=["GET", "POST"])
@login_required
def dashboard():
    user_ID = session["user_id"]
    results = MatchView.query.filter_by(user_id=user_ID).all()
    return render_template("dashboard.html", results=results)


@properties.route("/dashboard/delete", methods=["GET", "POST"])
def delete():
    if request.method == "POST":
        Property_id = request.form.get("property_id")
    return render_template("delete.html", property_id=Property_id)


@properties.route("/dashboard/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        Property_id = request.form.get("property_id")
    result = Properties.query.filter_by(id=Property_id)
    return render_template("edit.html", result=result)
