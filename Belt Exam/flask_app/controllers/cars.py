from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.car import Car
from flask_app.models.user import User


@app.route('/dashboard/')
def user_dashboard():
    user = User.get_one(session['user_id'])
    users_cars = Car.get_cars_with_seller()
    return render_template('dashboard.html', user=user, users_cars=users_cars)

@app.route('/view/<int:id>')
def show_car(id):
    car = Car.get_one(id)
    seller = User.get_one(car.user_id)
    return render_template('view.html', car=car, seller=seller)

@app.route('/new')
def new_car():
    return render_template('new.html')

@app.post('/create')
def create_listing():
    if not Car.is_valid_car(request.form):
        return redirect('/new')
    Car.create_car(request.form)
    
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def purchase_car(id):
    Car.delete_car(id)
    return redirect('/dashboard')

@app.route('/edit/<int:id>')
def edit_car(id):
    car = Car.get_one(id)
    session['car_id'] = id
    return render_template('edit.html', car=car)

@app.post('/submit_edit')
def submit_edit():
    if not Car.is_valid_car(request.form):
        return redirect(f'/edit/{session["car_id"]}')
    Car.edit_car(request.form)
    return redirect('/dashboard')