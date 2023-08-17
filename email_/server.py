from flask import Flask, render_template, redirect, session, request
# from emails import Email

app = Flask(__name__)
app.secret_key = "Bleh"

@app.route("/")
def index():
    return render_template("index.html")

@app.post("/success")

if __name__ == "__main__":
    app.run(debug=True)