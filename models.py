#DATABASE MODELS

from website import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer,primary_key=True) #primary key
    data = db.Column(db.String(10000)) #data of the note
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #date of the note
    user_id = db.Column(db.Integer,db.ForeignKey('user.id')) #foreign key

class User(db.Model, UserMixin):
    id = db.Column(db.Integer,primary_key=True) #primary key
    email = db.Column(db.String(150),unique=True) #unique email for every user
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    notes = db.relationship('Note') #relationship with the Note class
