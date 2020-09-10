from flask_login import LoginManager
from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()


#
# Initialization
#


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'b21b9e3d501093049b4f80032719962b41281700fe1a0829' # Just a urandom(24).hex()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.route('/error')
    @login_manager.unauthorized_handler
    def unauthorized():
        return redirect(url_for('main.error'))

    return app
