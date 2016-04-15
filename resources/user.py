# coding=utf-8
from flask.ext.login import logout_user, login_user, current_user
from flask import redirect, url_for, request, flash, Blueprint, render_template, session

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


@user_resource.route('/change_password', methods=['POST'])
def change_password():
    new_password = request.form['new_password']
    if new_password != request.form['new_password_repeat']:
        flash(u"Nytt passord stemmer ikke med det repiterte passordet")
        return redirect(url_for('main_resource.profile'))
    user_id = current_user.get_id()
    old_password = request.form['old_password']
    # must hash old password
    registered_user = User.query.filter_by(id=user_id, password=old_password).first()
    if registered_user is None:
        flash(u"Gammelt passord stemmer ikke")
        return redirect(url_for('main_resource.profile'))
    # must hash new password first
    registered_user.password = new_password
    db.session.commit()
    flash(u"Ditt passord er nå endret")
    return redirect(url_for('main_resource.profile'))


@user_resource.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = current_user.get_id()
    old_password = request.form['old_password']
    # must hash old password
    registered_user = User.query.filter_by(id=user_id, password=old_password).first()
    if registered_user is None:
        flash(u"Gammelt passord stemmer ikke")
        return redirect(url_for('main_resource.profile'))
    db.session.delete(registered_user)
    db.session.commit()
    flash(u"Din bruker er nå slettet")
    return redirect(url_for('user_resource.login'))
