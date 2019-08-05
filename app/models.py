from . import db
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__='users'
   
    # id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),index = True)
    email= db.Column(db.String(255),unique = True, index = True)
    id = db.Column(db.Integer, primary_key=True)
    pass_secure = db.Column(db.String(100))
    pitch=db.relationship('Pitches',backref='user',lazy='dynamic')
    profile_pic_path= db.Column(db.String())
    code = db.Column(db.Integer)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

class Pitches(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(250))
    description=db.Column(db.String(250))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    



class Comments(db.Model):
    __tablename__='comments'
    id=db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(250))
    # comment= db.Column(db.String())
   

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))