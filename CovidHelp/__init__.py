from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '1afd28ad58fb19cb088674114a5e9af9'
# For sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# For PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'admin_login'
login_manager.login_message_category = 'alert alert-success'


from CovidHelp import routes
