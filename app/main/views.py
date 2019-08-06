
from flask import render_template,url_for,request,abort,redirect
from flask_login import login_required
from . import main
from .. import db
from ..models import User,Pitch,Comment
from .forms import PitchForm, UpdateProfile


import markdown2




@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitching site Online'

    # search_pitch = request.args.get('pitch_query')
    # pitches= Pitch.get_all_pitches()

    return render_template('index.html', title = title)

#this section consist of the category root functions
@main.route('/categories/<int:id>')
def category(id):
   category_ = Category.query.get(id)
   pitches = Pitch.query.filter_by(category=category_.id).all()
   # pitches=Pitch.get_pitches(id)
   # title = f'{category.name} page'
   return render_template('category.html', pitches=pitches, category=category_)

@main.route('/coding/pitches/')
def coding():
    '''
    View root page function that returns the index page and its data
    '''
    
    pitches=Pitch.query.filter_by(category='coding')
    title = 'Home - Welcome to The best Pitching Website Online'  
    return render_template('coding.html', title = title, pitches=pitches)

@main.route('/poetry/pitches/')
def poetry():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'poetry'

    pitches=Pitch.query.filter_by(category='poetry')

    return render_template('poetry.html', title = title, pitches= pitches )

@main.route('/intelligence/pitches/')
def intelligence():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'intelligence pitches'

    pitches=Pitch.query.filter_by(category='intelligence')

    return render_template('intelligence.html', title = title, pitches= pitches )

@main.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):

    '''
    View pitch page function that returns the pitch details page and its data
    '''
    found_pitch= get_pitch(pitch_id)
    title = pitch_id
    pitch_comments = Comment.get_comments(pitch_id)

    return render_template('pitch.html',title= title ,found_pitch= found_pitch, pitch_comments= pitch_comments)

@main.route('/search/<pitch_name>')
def search(pitch_name):
    '''
    View function to display the search results
    '''
    searched_pitches = search_pitch(pitch_name)
    title = f'search results for {pitch_name}'

    return render_template('search.html',pitches = searched_pitches)


@main.route("/post/new", methods= ['GET', 'POST'])
@login_required
def new_pitch():

    forms = PitchForm()
    if forms.validate_on_submit():
        pitch = Pitch(title=forms.title.data, category = forms.category.data)
        db.session.add(pitch)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    return render_template('new_pitch.html',title = 'New Post',new_pitch_form = forms)

@main.route('/pitch/comments/new/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentsForm()
    vote_form = UpvoteForm()
    if form.validate_on_submit():
        new_comment = Comment(pitch_id =id,comment=form.comment.data,username=current_user.username,votes=form.vote.data)
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    #title = f'{pitch_result.id} review'
    return render_template('new_comment.html',comment_form=form, vote_form= vote_form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    
    return render_template('profile/update.html',form =form)

@main.route('/view/comment/<int:id>')
def view_comments(id):
    '''
    Function that returns  the comments belonging to a particular pitch
    '''
    comments = Comment.get_comments(id)
    return render_template('view_comments.html',comments = comments, id=id)



@main.route('/test/<int:id>')  
def test(id):
    '''
    this is route for basic testing
    '''
    pitch =Pitch.query.filter_by(id=1).first()
    return render_template('test.html',pitch= pitch)
5