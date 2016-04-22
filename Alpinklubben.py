# coding=utf-8
from flask import Flask, redirect, url_for, g
from flask.ext.login import LoginManager, current_user
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig

from resources.chart import chart_resource
from resources.main import main_resource
from resources.user import user_resource
from resources.shop import shop_resource
from entities.shared import db
from entities.user import User

# global variables
DATABASE = 'test.db'
DEBUG = True
SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

app = Flask(__name__)

app.register_blueprint(user_resource)
app.register_blueprint(shop_resource)
app.register_blueprint(main_resource)
app.register_blueprint(chart_resource)

app.secret_key = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'user_resource.login'
login_manager.login_message = u"Du må logge inn for å nå denne siden."


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.before_request
def before_request():
    g.user = current_user


@app.route('/')
def index():
    return redirect(url_for('main_resource.shop'))


if __name__ == '__main__':
    AppConfig(app)
    Bootstrap(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + DATABASE
    db.init_app(app)
    with app.app_context():
        db.metadata.create_all(db.engine)
    app.config['BOOTSTRAP_SERVE_LOCAL'] = True
    app.run(debug=DEBUG)
