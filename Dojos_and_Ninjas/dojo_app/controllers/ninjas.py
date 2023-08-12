from flask import Flask, render_template, redirect, request
from dojo_app import app
from dojo_app.models.ninja import Ninja

@app.route('/ninjas')
def get_all_ninjas():
    ninjas = Ninja.get_all()
    return render_template('ninjas.html', ninjas=ninjas)

@app.route('')