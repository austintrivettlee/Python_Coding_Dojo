from flask import Flask, render_template, redirect, request
from emails import Email

app = Flask(__name__)
app.secret_key = "Bleh"

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/new")
def new():
    if not Email.is_valid_email(request.form):
        return redirect('/')
    Email.create(request.form)
    return redirect("/success")

@app.route("/success")
def success():
    emails = Email.get_all()
    return render_template("success.html", emails=emails)

if __name__ == "__main__":
    app.run(debug=True)