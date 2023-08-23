from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.comment import Comment

@app.route('/new')
def comment():
    if not 'user_id' in session:
        flash('Stop trying to infiltrate my website or the space dragons will be released.')
        return redirect('/')
    return render_template('comment.html')

@app.post('/post')
def post_comment():
    if not Comment.validate_comment(request.form):
        return redirect('/new')
    Comment.create_comment(request.form)
    return redirect('/dashboard')