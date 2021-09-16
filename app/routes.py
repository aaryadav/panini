from flask import render_template, flash, redirect, url_for, request
from app import app, db
from app.forms import LoginForm
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.urls import url_parse
from app.models import User
from app.forms import RegistrationForm, EditProfileForm
from datetime import datetime

@app.route('/')
@app.route('/home')
def home():
  return render_template('base.html', title = 'panini')

@app.route('/login')
def login():
  form = LoginForm()
  return render_template('login.html', title = 'login - panini', form=form)

# @app.route('/signup')
# @app.route('/register')
# def signup():
  # return render_template('signup.html', title = 'signup - panini')

if __name__ == "__main__":  
	app.run(
		host='0.0.0.0',
		# port=random.randint(2000, 9000)
  )
