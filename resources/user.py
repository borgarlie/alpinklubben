# coding=utf-8
from flask.ext.login import logout_user, login_user
from flask import redirect, url_for, request, flash, Blueprint, render_template

from entities.shared import db
from entities.user import User

user_resource = Blueprint('user_resource', __name__, template_folder='templates')


# need to handle errors here :: integritity error etc!
# password needs to be hashed
@user_resource.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', page="register")
    user = User(request.form['username'], request.form['password'], request.form['email'])
    db.session.add(user)
    db.session.commit()
    flash('Bruker registrert')
    return redirect(url_for('user_resource.login'))


@user_resource.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', page="login")
    username = request.form['username']
    password = request.form['password']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    # need to hash the password
    registered_user = User.query.filter_by(username=username, password=password).first()
    if registered_user is None:
        flash('Feil brukernavn eller passord', 'error')
        return redirect(url_for('user_resource.login'))
    login_user(registered_user, remember=remember_me)
    flash(u'Du er nå logget inn!')
    return redirect(request.args.get('next') or url_for('index'))


@user_resource.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
