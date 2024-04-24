from flask import render_template
from flaskblog import app
from flaskblog.forms import loginForm, registerForm


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    form = loginForm()
    return render_template('login.html', form=form)

@app.route('/signup')
def register():
    form = registerForm()
    return render_template('signup.html', form=form)