from flask import render_template, request, Blueprint, redirect, url_for
from models import db
from models.models import Users

authentication = Blueprint("authentication", __name__, static_folder="static", template_folder="templates")

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')