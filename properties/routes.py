from flask import render_template, request, Blueprint, redirect, url_for
from models import db
from models.models import Properties, Clients, Users

properties = Blueprint("properties", __name__, static_folder="static", template_folder="templates")
    
@properties.route('/addproperty', methods=['GET', 'POST'])
def addproperties():
    if request.method == 'POST':
        address1 = request.form.get('address1')
        address2 = request.form.get('address2')
        city = request.form.get('city')
        state = request.form.get('state')
        price = float(request.form.get('price'))
        bedrooms = float(request.form.get('bedrooms'))
        bathrooms = float(request.form.get('bathrooms'))
        comments = request.form.get('comments')

        new_property = Properties(
            address1 = address1,
            address2 = address2,
            city = city,
            state = state,
            price = price,
            bedrooms = bedrooms,
            bathrooms = bathrooms,
            comments = comments
        )

        db.session.add(new_property)
        db.session.commit()
        return redirect(url_for('search'))
    return render_template('addproperty.html')

@properties.route('/addclient', methods=['GET', 'POST'])
def addclients():
    if request.method == 'POST':
        contact = request.form.get('contact')
        city = request.form.get('city')
        state = request.form.get('state')
        price = float(request.form.get('price'))
        bedrooms = float(request.form.get('bedrooms'))
        bathrooms = float(request.form.get('bathrooms'))
        comments = request.form.get('comments')

        new_client = Clients(
            contact = contact,
            city = city,
            state = state,
            price = price,
            bedrooms = bedrooms,
            bathrooms = bathrooms,
            comments = comments
        )

        db.session.add(new_client)
        db.session.commit()
        return redirect(url_for('search'))
    return render_template('addclient.html')

@properties.route('/portfolio', methods=['GET', 'POST'])
def portflio():
    return "This is your Portfolio!", 200