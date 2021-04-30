from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '1afd28ad58fb19cb088674114a5e9af9'
# For sqlite
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# For PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:steelchair111@localhost/CovidHelpAgra'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from CovidHelp import routes
