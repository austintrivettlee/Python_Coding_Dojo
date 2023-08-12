from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.user import User

@app.route('/')
def get_all_users():
    users = User.get_all()
    return render_template("index.html", users=users)

@app.get('/user/<int:user_id>')
def get_one_user(user_id):
    user = User.get_one(user_id)
    return render_template("show.html", user=user)

@app.get("/users/new")
def new_friend():
    """Displays the new user form"""
    
    return render_template('create.html')

@app.post('/users/create')
def create_user():
    user_id = User.create(request.form)
    return redirect(f'/user/{user_id}')

@app.get('/user/<int:user_id>/delete')
def delete_user(user_id):
    User.delete(user_id)
    return redirect('/')

@app.get('/user/<int:user_id>/edit')
def edit_user(user_id):
    user = User.get_one(user_id)
    return render_template('edit.html', user=user)

@app.post('/user/<int:user_id>/update')
def update_user(user_id):
    User.update(request.form)
    return redirect(f'/user/{user_id}')