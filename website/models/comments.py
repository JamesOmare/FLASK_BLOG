from ..utils import db
from sqlalchemy.sql import func

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(250), nullable = False)
    date_created = db.Column(db.DateTime (timezone = True), default = func.now())
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete = 'CASCADE'), nullable= False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id', ondelete = 'CASCADE'), nullable= False)