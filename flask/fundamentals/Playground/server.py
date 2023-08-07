from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def got_to_play():
    return "Go To /Play or /Play/(x) where x can be any number you want!"

@app.route('/play')
def run_playground():
    return render_template('index.html')

@app.route('/play/<num>')
def run_playground_times(num):
    return render_template('index.html', boxes=int(num))

@app.route('/play/<num>/<color>')
def run_playground_times_and_color(num, color):
    return render_template('index.html', boxes=int(num), box_color=color)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)