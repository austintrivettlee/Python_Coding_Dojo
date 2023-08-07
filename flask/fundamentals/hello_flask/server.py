from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html', phrase="hello", times = 5)

@app.route('/dojo')
def hello_dojo():
    return "Hello Dojo"

@app.route('/say/<name>')
def hello(name):
    return f"Hello, {name}!"

@app.route('/repeat/<num>/<word>')
def repeat(num, word):
    output = ""
    for i in range(int(num)):
        output += word + " "
    return output

@app.errorhandler(404)
def not_found(e):
    return "Houston we have a problem!"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)



