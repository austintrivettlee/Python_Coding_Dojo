from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    if 'num' not in session:
        session['num'] = 0
    session['num'] += 1
    session['counter'] +=1
    return render_template('index.html', num=session['num'], counter=session['counter'])

@app.route('/addtwo')
def add_two():
    session['num'] += 1
    return redirect('/')

@app.route('/custom', methods=['POST'])
def custom():
    session['num'] += (int(request.form['customnum'])-1)
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session['num'] = 0
    return redirect('/')

@app.route


if __name__ == "__main__":
    app.run(debug=True)