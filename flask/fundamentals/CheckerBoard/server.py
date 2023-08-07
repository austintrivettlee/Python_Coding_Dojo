from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', rows=8, columns=8)

@app.route('/<num>')
def user_input(num):
    return render_template('index.html', rows=int(num), columns=8)

@app.route('/<num1>/<num2>')
def user_input_coordinate(num1, num2):
    return render_template('index.html', rows=int(num1), columns=int(num2))

@app.route('/<num1>/<num2>/<color1>/<color2>')
def user_input_coordinate_color(num1, num2, color1, color2):
    return render_template('index.html', rows=int(num1), columns=int(num2), first_color=color1, second_color=color2)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)