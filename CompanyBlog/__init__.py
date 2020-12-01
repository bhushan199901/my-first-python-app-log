from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'


###################################################################
##DATABASE SETUP######
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)
Migrate(app, db)

# LOGIN CONFIGS
# setup login Manager(object creation)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'


# to register blueprint from core.view.core
from CompanyBlog.core.views import core

app.register_blueprint(core)


# to register blueprint from error_page.handlers.err_pages
from CompanyBlog.error_pages.handlers import err_pages
app.register_blueprint(err_pages)

# to register the users.view - user blueprint
from CompanyBlog.users.views import users
app.register_blueprint(users)

# to register blog_posts
from CompanyBlog.blog_posts.views import blog_posts
app.register_blueprint(blog_posts)
