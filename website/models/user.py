from ..utils import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    username = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime (timezone = True), default = func.now())
    posts = db.relationship('Post', backref = 'user', passive_deletes = True)
    comments = db.relationship('Comment', backref = 'user', passive_deletes = True)
    likes = db.relationship('Like', backref = 'user', passive_deletes = True)

