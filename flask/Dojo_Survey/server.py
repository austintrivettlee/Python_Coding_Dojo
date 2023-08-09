from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/results", methods=["POST"])
def show_results():
    session['full_name'] = request.form['full_name']
    session['location'] = request.form.getlist('location')
    session['favlang'] = request.form['favlang']
    session['comments'] = request.form['comments']
    return render_template("results.html")


@app.route("/reset")
def reset_page():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
