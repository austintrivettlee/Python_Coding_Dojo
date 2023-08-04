from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """
    this is the root route
    """

    name = "Austin"

    return render_template("index.html", name=name)


@app.route("/<name>")
def name(person):
    """
    This is a dynamic route that displays the name passed into the URL
    """

    return render_template("index.html", name=person)
if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)