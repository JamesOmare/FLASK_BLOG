from ..utils import db
from sqlalchemy.sql import func

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable = False)
    date_created = db.Column(db.DateTime (timezone = True), default = func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable= False)
    comments = db.relationship('Comment', backref = 'post', passive_deletes = True)