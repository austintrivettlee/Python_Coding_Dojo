from flask import render_template, redirect, request
from dojo_app import app
from dojo_app.models.dojo import Dojo
from dojo_app.models.ninja import Ninja


@app.route('/')
def redirect_to_main():
    return redirect('/dojos')

@app.route('/dojos')
def show_dojos():
    dojos = Dojo.get_all_dojos()
    return render_template('index.html', dojos=dojos)

@app.post('/dojos/create')
def create_new_dojo():
    Dojo.create_dojo(request.form)
    return redirect("/dojos")

@app.route('/dojos/<int:id>')
def show_dojos_ninjas(id):
    dojo = Dojo.get_one_dojo_with_ninjas(id)
    dojo_name = Dojo.get_one_dojo(id)
    return render_template('dojo.html', dojo=dojo, dojo_name=dojo_name)