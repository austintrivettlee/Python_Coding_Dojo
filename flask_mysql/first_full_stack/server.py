from flask import Flask, render_template, request, session, redirect
from pprint import pprint

# import the class from friend.py
from friend import Friend

app = Flask(__name__)


@app.route('/')
def index():
    friends = Friend.get_all()
    print(friends)
    return render_template("index.html", friends = friends)

@app.route('/friends/<int:friend_id>')
def details(friend_id):
    """displays the details of one friend"""
    friend = Friend.get_one(friend_id)
    return render_template("details.html", friend = friend)

@app.post('/friends/create')
def create_friend():
    """Process the submitted form which creates a row in friend table"""

    friend_id = Friend.create(request.form)
    return redirect(f"/friends/{friend_id}")

@app.get("/friends/new")
def new_friend():
    """Displays the new friend form template"""
    
    return render_template('new.html')

@app.route('/friends/<int:friend_id>/edit')
def edit_friend(friend_id):
    """Displays the edit form friend template"""
    
    friend = Friend.get_one(friend_id)
    
    return render_template('edit.html' , friend=friend)

@app.post("/friends/<int:friend_id>/update")
def update_friend(friend_id):
    """ Processes the update to the friend. """

    Friend.update(request.form)
    return redirect(f"/friends/{friend_id}")

@app.route("/friends/<int:friend_id>/delete")
def delete_friend(friend_id):
    
    Friend.delete(friend_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
