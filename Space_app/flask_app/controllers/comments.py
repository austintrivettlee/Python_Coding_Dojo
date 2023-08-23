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
    return redirect(f'/dashboard/{session["user_id"]}')

@app.route('/dashboard')
def dashboard():
    if not 'user_id' in session:
        flash('Stop trying to infiltrate my website or the space dragons will be released.')
        return redirect('/')
    elif 'user_id' in session:
        return redirect(f'/dashboard/{session["user_id"]}')

@app.route('/dashboard/<int:id>')
def user_dashboard(id):
    if not 'user_id' in session:
        flash('Stop trying to infiltrate my website or the space dragons will be released.')
        return redirect('/')
    user = User.get_one(id)
    User.get_one(session['user_id'])
    comments = Comment.get_all_with_creator()
    return render_template('dashboard.html', user=user, comments=comments)

