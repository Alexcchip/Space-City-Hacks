import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_migrate import Migrate
from forms import ChatForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '!@#$%^&*'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

Migrate(app, db)

class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    password = db.Column(db.Text)
    email = db.Column(db.Text)

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    
    def __repr__(self):
        return "{} has email {} and password{}".format(self.name, self.email, self.password)

##########################
####VIEW FUNCTIONS########
##########################

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    name = request.args.get('name')
    email = request.args.get('email')
    pwd = request.args.get('password')
    if(name != None):
        new_user= users(name, email, pwd)
        db.session.add(new_user)
        db.session.commit()
    else:
        user = users.query.filter_by(email = email).first()
        print(user)
        if(user is not None):
            print("yes")
#            redirect(url_for())
        else:
            print('no')
    return render_template('login.html')

@app.route('/chat', methods = ['GET', 'POST'])
def chat():
    form = ChatForm()
    print("Good")
    if form.validate_on_submit():
        pass
    return render_template('chat.html', form = form)

if __name__ == '__main__':
    app.run(debug = True)
