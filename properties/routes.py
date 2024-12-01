from flask import render_template, request, Blueprint, redirect, url_for, session
from models import db
from models.models import Properties, Clients, Users, MatchView
from flask_login import LoginManager, login_required

properties = Blueprint("properties", __name__, template_folder="templates", static_folder="static")
    
@properties.route('/add-property', methods=['GET', 'POST'])
@login_required
def addproperties():
    if request.method == 'POST':
        # address1 = request.form.get('address1')
        # address2 = request.form.get('address2')
        # city = request.form.get('city')
        # state = request.form.get('state')
        # zipcode = float(request.form.get('zipcode'))
        # price = float(request.form.get('price'))
        # bedrooms = float(request.form.get('bedrooms'))
        # bathrooms = float(request.form.get('bathrooms'))
        # comments = request.form.get('comments')

        # new_property = Properties(
        #     address1 = address1,
        #     address2 = address2,
        #     city = city,
        #     state = state,
        #     zipcode = zipcode,
        #     price = price,
        #     bedrooms = bedrooms,
        #     bathrooms = bathrooms,
        #     comments = comments,
        #     user_id = session['user_id']
        # )
        # db.session.add(new_property)
        # db.session.commit()
        return render_template('search.html')
    return render_template('addproperty.html')

@properties.route('/add-client', methods=['GET', 'POST'])
@login_required
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
            comments = comments,
            user_id = session['user_id']
        )

        db.session.add(new_client)
        db.session.commit()
        return redirect(render_template('search.html'))
    return render_template('addclient.html')

@properties.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        city = request.form.get('city')
        zipcode = request.form.get('zipcode')
        price = request.form.get('price')
        bedrooms = request.form.get('bedrooms')
        bathrooms = request.form.get('bathrooms')
        results = Properties.query.all()
        return render_template('search.html', results = results)
    
    return render_template('search.html')

@properties.route('/dashboard', methods = ['GET', 'POST'])
@login_required
def dashboard():
    user_ID = session['user_id']
    results = MatchView.query.filter_by(user_id=user_ID).all()
    # if request.method == 'POST':
    #     pass
    return render_template('dashboard.html' , results = results)