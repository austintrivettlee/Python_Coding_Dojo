from flask import render_template, redirect, request
from dojo_app import app
from pprint import pprint
from dojo_app.models.ninja import Ninja
from dojo_app.models.dojo import Dojo

@app.route('/ninjas')
def get_all_ninjas():
    ninjas = Ninja.get_all_ninjas()
    return render_template('ninjas.html', ninjas=ninjas)

@app.route('/ninjas/add')
def add_ninja():
    dojos = Dojo.get_all_dojos()
    "Displays the New Ninja Form"
    return render_template('add_ninja.html', dojos=dojos)

@app.post('/ninjas/create')
def create_new_ninja():
    dojo_id = Ninja.get_one_ninja(Ninja.create_ninja(request.form))
    return redirect(f'/dojos/{dojo_id.dojo_id}')