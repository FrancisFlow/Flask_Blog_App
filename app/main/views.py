from flask import render_template,request,redirect,url_for,abort,flash,session
from . import main
from flask_login import login_required,current_user
from ..models import User, Blog, Comment
from .forms import UpdateProfile
from .. import db


@main.route('/')
def index():
    title='The Blog'
    return render_template('index.html', title=title)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    title = f'{uname} Profile'
    return render_template('profile/profile.html', user=user, title=title)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
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
    title = 'Update | Profile'
    return render_template('profile/update.html',form=form, title=title)
