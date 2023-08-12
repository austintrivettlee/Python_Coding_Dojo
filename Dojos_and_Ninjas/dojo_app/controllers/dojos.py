from flask import Flask, render_template, redirect, request, flash
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
    flash(f'You added a Dojo!')
    return redirect("/dojos")