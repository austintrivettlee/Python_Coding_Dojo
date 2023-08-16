from flask import Flask, render_template, redirect, session, request
from dojos import Dojo

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/results", methods=["POST"])
def show_results():
    if not Dojo.validate_info(request.form):
        return redirect("/")
    dojo = Dojo.get_one(Dojo.add_info(request.form))
    return render_template("results.html", dojo=dojo)


@app.route("/reset")
def reset_page():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
