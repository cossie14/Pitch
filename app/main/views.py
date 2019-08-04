
from flask import render_template,url_for,request,abort,redirect
from flask_login import login_required
from . import main
from .forms import Pitch
from .. import db
from ..models import User,Pitches,Comments

@main.route('/')
def index():
  user = User.query.filter_by(username='uname').first()
  pitches = Pitches.query.all()
  title = 'Welcome to pitch'
  message = 'Cool pitches'
  return render_template('index.html',message = message,title= title,pitches = pitches, user=user)

@main.route('/user/<uname>',methods=['GET','POST'])
@login_required
def profile(uname):
  user = User.query.filter_by(username=uname).first()
  pitches=Pitches.query.filter_by(user_id=user.id)
  if user is None:
    abort(404)
  title = f'{user.username}'
  return render_template('profile/profile.html',title=title,user = user,pitches=pitches)

@main.route('/pitches/<uname>', methods=['GET','POST'])
@login_required
def pitches(uname):
  pitch_form = Pitch()
  user = User.query.filter_by(username = uname).first()
  if pitch_form.validate_on_submit():
    pitch = Pitches(title = pitch_form.title.data, description = pitch_form.description.data,user = user)
    db.session.add(pitch)
    db.session.commit()
    return redirect(url_for('main.index'))
  title='Pitches'
  return render_template('pitch.html',title=title,pitch_form=pitch_form)