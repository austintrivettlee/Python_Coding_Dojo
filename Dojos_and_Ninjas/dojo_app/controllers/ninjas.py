from flask import Flask, render_template, redirect, request
from dojo_app import app
from dojo_app.models.ninja import Ninja
from dojo_app.models.dojo import Dojo

@app.route('/ninjas')
def get_all_ninjas():
    ninjas = Ninja.get_all()
    return render_template('ninjas.html', ninjas=ninjas)

@app.route('/ninjas/add')
def add_ninja():
    dojos = Dojo.get_all_dojos()
    "Displays the New Ninja Form"
    return render_template('add_ninja.html', dojos=dojos)

@app.post('/ninjas/create')
def create_new_ninja():
    Ninja.create_ninja(request.form)
    return redirect('/ninjas')