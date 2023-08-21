from flask import render_template, redirect, request
from reg_app import app
from reg_app.models.user import User

@app.route('/')
def index():
    return render_template("index.html")