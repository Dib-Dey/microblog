from app import flask_app
from flask import render_template
from app.flask_form import LoginForm

#the route() decorator to tell Flask what URL should trigger our function.
@flask_app.route('/')
@flask_app.route('/index')
def index():
    user = {"username":"ddey"}
    title = "Flask Example:"
    return render_template('index.html', title=title, user= user)

@flask_app.route('/form')
def form():
    form = LoginForm()
    return render_template('form.html',form = form, title="Login Form")