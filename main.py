
from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#import random, string

app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static',
)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


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
