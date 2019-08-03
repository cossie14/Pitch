from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index = True)
    email= db.Column(db.String(255),unique = True, index = True)
    pass_secure = db.Column(db.String(100))
    pitches=db.relationship('Pitch',backref='user',lazy='dynamic')
    profile_pic_path= db.Column(db.String())
    code = db.Column(db.Integer)