from datetime import datetime

from flask import current_app
from flask_login import UserMixin, current_user
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView

from stp import login_manager, db

@login_manager.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))

class user(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    phone_no = db.Column(db.Integer)
    email = db.Column(db.String(120), unique=True, nullable=False)

    # user_starups = db.relationship('starups', backref='author', lazy=True)
    # user_investors = db.relationship('', backref='author', lazy=True)
    # user_incubators = db.relationship('', backref='author', lazy=True)
    user_posts = db.relationship('post', backref='author', lazy=True)

    def __repr__(self):
        return "{}-{}".format(username, email)

class posts(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"





# class startups(db.Model):
#     __tablename__ = "startups"
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     location = db.Column(db.String(20), nullable=False)
#     description = db.Column(db.String(500))
#     services =
#
#
# class investors(db.Model):
#     __tablename__ = "investors"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     location = db.Column(db.String(20), nullable=False)
#
#
#
# class incubators(db.Model):
#     __tablename__ = "incubators"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False)
#     location = db.Column(db.String(20), nullable=False)
#
#
#
# class user(db.Model):
#     __tablename__ = "user"
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(50), unique=True, nullable=False
#     location = db.Column(db.String(20), nullable=False))
