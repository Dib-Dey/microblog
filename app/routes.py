from app import flask_app
from flask import render_template
from flask import flash
from flask import redirect
from app.form import LoginForm

#the route() decorator to tell Flask what URL should trigger our function.
@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {"username":"ddey"}
    title = "Flask Example:"
    return render_template('index.html', title=title, user= user)

@flask_app.route('/form', methods = ['GET', 'POST'])
def log():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('form.html',form = form, title="Login Form")