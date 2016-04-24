# coding=utf-8

import sqlite3

import sqlalchemy
from flask.ext.login import logout_user, login_user, current_user
from flask import redirect, url_for, request, flash, Blueprint, render_template
from werkzeug.security import generate_password_hash, check_password_hash

from entities.shared import db
from entities.user import User

user_resource = Blueprint('user_resource', __name__, template_folder='templates')


@user_resource.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html', page="register")
    pw_hash = generate_password_hash(request.form['password'])
    user = User(request.form['username'], pw_hash, request.form['year_born'], request.form['email'])
    try:
        db.session.add(user)
        db.session.commit()
        flash('Bruker registrert')
    except sqlalchemy.exc.IntegrityError:
        flash(u'Brukernavn eller epostadressen finnes allerede.')
        return render_template('register.html', page="register")
    return redirect(url_for('user_resource.login'))


@user_resource.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html', page="login")
    username = request.form['username']
    remember_me = False
    if 'remember_me' in request.form:
        remember_me = True
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None or not check_password_hash(registered_user.password, request.form['password']):
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
    registered_user = User.query.filter_by(id=user_id).first()
    if registered_user is None or not check_password_hash(registered_user.password, request.form['old_password']):
        flash(u"Gammelt passord stemmer ikke")
        return redirect(url_for('main_resource.profile'))
    new_password_hash = generate_password_hash(new_password)
    registered_user.password = new_password_hash
    db.session.commit()
    flash(u"Ditt passord er nå endret")
    return redirect(url_for('main_resource.profile'))


@user_resource.route('/delete_user', methods=['POST'])
def delete_user():
    user_id = current_user.get_id()
    registered_user = User.query.filter_by(id=user_id).first()
    if registered_user is None or not check_password_hash(registered_user.password, request.form['old_password']):
        flash(u"Passordet stemmer ikke")
        return redirect(url_for('main_resource.profile'))
    db.session.delete(registered_user)
    db.session.commit()
    flash(u"Din bruker er nå slettet")
    return redirect(url_for('user_resource.login'))
