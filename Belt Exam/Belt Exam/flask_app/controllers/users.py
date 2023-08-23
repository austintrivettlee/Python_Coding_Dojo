from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.car import Car
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if session['user_id']:
        return redirect('/dashboard')
    return render_template("index.html")

@app.post('/register')
def register_user():
    if not User.is_valid_user(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": pw_hash
    }
    
    user_id = User.create(data)
    
    session['user_id'] = user_id
    flash("Thanks for Registering!")
    return redirect('/dashboard')

@app.post('/login')
def login():
    data = { "email": request.form['email'] }
    user_in_db = User.get_by_email(data)
    if len(request.form['email']) < 1:
        flash('Email cannot be left blank.')
        return redirect('/')
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if len(request.form['password']) < 1:
        flash('Password cannot be left blank.')
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email/Password')
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out!')
    return redirect('/')
