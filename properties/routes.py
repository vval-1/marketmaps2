from flask import render_template, request, Blueprint, redirect, url_for, session
from models import db
from models.models import Properties, Clients, Users, MatchView
from flask_login import LoginManager, login_required

properties = Blueprint(
    "properties", __name__, template_folder="templates", static_folder="static"
)


@properties.route("/add-property", methods=["GET", "POST"])
@login_required
def addproperties():
    if request.method == "POST":
        address1 = request.form.get("address1", None)
        property_type = request.form.get("property_type", None)
        city = request.form.get("city", None)
        min_price = float(request.form.get("min_price")) if request.form.get("min_price") not in ["", None] else None
        max_price = float(request.form.get("max_price")) if request.form.get("max_price") not in ["", None]else None
        bedrooms = float(request.form.get("bedrooms")) if request.form.get("bedrooms") not in ["", None] else None
        bathrooms = float(request.form.get("bathrooms")) if request.form.get("bathrooms") not in ["", None] else None
        facing_direction = request.form.get("facing_direction", None)
        min_sqft = float(request.form.get("min_sqft")) if request.form.get("min_sqft") not in ["", None] else None
        max_sqft = float(request.form.get("max_sqft"))if request.form.get("max_sqft") not in ["", None] else None
        possession = request.form.get("possession", None)
        is_gated = request.form.get("is_gated", None)
        uds = float(request.form.get("uds")) if request.form.get("uds") not in ["", None] else None
        plot_size = float(request.form.get("plot_size")) if request.form.get("plot_size") not in ["", None] else None
        land_size = float(request.form.get("land_size")) if request.form.get("land_size") not in ["", None] else None
        price_per_acre = float(request.form.get("price_per_acre")) if request.form.get("price_per_acre") not in ["", None] else None
        type_of_ownership = request.form.get("type_of_ownership", None)
        purpose = request.form.get("purpose", None)
        agent_name = request.form.get("agent_name", None)
        agent_phone = float(request.form.get("agent_phone")) if request.form.get("agent_role") not in ["", None] else None
        agent_role = request.form.get("agent_role", None)

        new_property = Properties(
            address1=address1,
            property_type=property_type,
            city=city,
            min_price=min_price,
            max_price=max_price,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            facing_direction=facing_direction,
            min_sqft=min_sqft,
            max_sqft=max_sqft,
            possession=possession,
            is_gated=is_gated,
            uds=uds,
            plot_size=plot_size,
            land_size=land_size,
            price_per_acre=price_per_acre,
            type_of_ownership=type_of_ownership,
            purpose=purpose,
            agent_name=agent_name,
            agent_phone=agent_phone,
            agent_role=agent_role,
            user_id=session["user_id"],
        )
        db.session.add(new_property)
        db.session.commit()
        return render_template("search.html")
    return render_template("addproperty.html")


@properties.route("/add-client", methods=["GET", "POST"])
@login_required
def addclients():
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
        Property_id = request.form.get('property_id')
    return render_template("delete.html", property_id = Property_id)

@properties.route("/dashboard/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        Property_id = request.form.get('property_id')
    return render_template("edit.html", property_id = Property_id)    