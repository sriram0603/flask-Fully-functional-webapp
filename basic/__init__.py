from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from basic.config import Config

db=SQLAlchemy()
bcrypt=Bcrypt()
login_manager = LoginManager() 
login_manager.login_view="users.login"
login_manager.login_message_category='info'

mail = Mail()




def create_app(config_app=Config):
	app=Flask(__name__)
	app.config.from_object(Config)
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app)
	mail.init_app(app)
	from basic.users.routes import users
	from basic.posts.routes import posts
	from basic.main.routes import main
	app.register_blueprint(users)
	app.register_blueprint(main)
	app.register_blueprint(posts)

	return app