import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SECRET_KEY'] = '!@#$%^&*'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

#############################
####VIEW FUNCTIONS###########
#############################

@app.route('/')
def home():
    return render_template('home.html')

#@app.route('/login')
#def login():
#    return render_template()


if __name__ == '__main__':
    app.run(debug = True)
