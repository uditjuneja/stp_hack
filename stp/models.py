from datetime import datetime
from flask import current_app
from flask_login import UserMixin, current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from stp import login_manager, db

@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))

class users(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    company = db.Column(db.String(60))
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    phone_no = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_priority = db.Column(db.Integer, default=2)

    # user_starups = db.relationship('starups', backref='author', lazy=True)
    # user_investors = db.relationship('', backref='author', lazy=True)
    # user_incubators = db.relationship('', backref='author', lazy=True)
    user_posts = db.relationship('posts', backref='author', lazy=True)

    def __repr__(self):
        return "{}-{}".format(self.username, self.email)

class posts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    heading = db.Column(db.String(100), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.heading}', '{self.content}', '{self.image_file}', '{self.date_posted}')"

class startups(db.Model):
    __tablename__ = "startups"

    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(50), unique=True, nullable=False)
    email= db.Column(db.String(50), unique=True, nullable=False)
    website = db.Column(db.String(50), unique=True, nullable=False)
    contact = db.Column(db.Integer(), unique=True, nullable=False)
    # image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    age= db.Column(db.Integer(), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(20), nullable=False)
    zipcode = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(500))

    def __repr__(self):
        return f"startup('{self.company}', '{self.email}', '{self.website}', '{self.description}')"

class investors(db.Model):
    __tablename__ = "investors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True,nullable=False)
    city = db.Column(db.String(50), nullable=False)
    investment = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"Post('{self.name}')"

class incubators(db.Model):
     __tablename__ = "incubators"

     name = db.Column(db.String(50), unique=True ,primary_key=True)
     location = db.Column(db.String(50), nullable=False)
     seats = db.Column(db.Integer, nullable=False)
     startup_incubated = db.Column(db.Integer, nullable=False)
     funding = db.Column(db.Integer, nullable=False)

     def __repr__(self):
         return f"Post('{self.name}')"
