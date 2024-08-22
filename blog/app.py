from flask import Flask

# from .admin import admin
from .models.database import db
from .views.users import users_app
from .views.articles import articles_app
from .views.index import index
from .views.auth import login_manager, auth_app
from .views.authors import authors_app
from flask_migrate import Migrate
from blog.security import flask_bcrypt
# from .api import init_api
from flask_wtf.csrf import CSRFProtect, CSRFError

VIEWS = [
    index,
    users_app,
    articles_app,
    auth_app,
    authors_app,
]


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)


# def create_app() -> Flask:
app = Flask(__name__)

csrf = CSRFProtect(app)

app.config.from_pyfile('configs.py')

db.init_app(app)
flask_bcrypt.init_app(app)
csrf.init_app(app)

migrate = Migrate(app, db, compare_type=True)

# register_extensions(app)
register_blueprints(app)

login_manager.init_app(app)

# admin.init_app(app)
# api=init_api(app)

# return app
