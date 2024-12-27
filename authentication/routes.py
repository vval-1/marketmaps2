from flask import render_template, request, Blueprint, redirect, url_for, session, flash 
from models import db
from models.models import Users
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, Email, Regexp
from flask_bcrypt import Bcrypt

authentication = Blueprint("authentication", __name__, static_folder="static", template_folder="templates")


class RegisterForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email(message="Invalid Email Address")])
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)])
    agent_name = StringField(validators=[InputRequired()])
    agent_phone = StringField(validators=[InputRequired(), Length(min=10, max=10, message="Phone number must contain exactly 10 digits"), Regexp('^\d+$', message="Phone number must contain only digits")])
    submit = SubmitField("Register")
        
class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), Length(min=4, max=20)])
    submit = SubmitField("Login")

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    from app import bcrypt #Fix circular import when possible 
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                session['user_id'] = user.id
                session['agent_name'] = user.agent_name
                session['agent_phone'] = user.agent_phone
                return redirect('/')
    return render_template('login.html', form=form)

@authentication.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    from app import bcrypt #Fix circular import when possible 
    if form.validate_on_submit():
        existing_user_email = Users.query.filter_by(email=form.email.data).first()
        if existing_user_email:
            flash("This Account Already Exists. Please Log in!")
            return redirect('/auth/login')
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        decoded_password = hashed_password.decode('utf-8') if isinstance(hashed_password, bytes) else hashed_password
        new_user = Users(email=form.email.data, username=form.username.data, password=decoded_password, agent_name=form.agent_name.data, agent_phone=form.agent_phone.data)
        db.session.add(new_user)
        db.session.commit()
        flash("Account Successfully Created, Please Log in!")
        return redirect('/auth/login')
    return render_template('register.html', form=form)

@authentication.route('/logout')
@login_required
def logout():
    session.clear() 
    logout_user()
    flash("You Have Been Successfully Logged Out!")
    return redirect('/auth/login')
