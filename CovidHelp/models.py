from CovidHelp import db, login_manager
from flask_login import UserMixin
import datetime

@login_manager.user_loader
def load_user(user_id):
    admin =  Admin.query.get(int(user_id))
    return admin if admin else None


class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(100))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    upvotes = db.Column(db.Integer, default=0, nullable=False)

    def __repr__(self):
        return f"Resource({self.id}, {self.name})"


class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"Service({self.id}, {self.name})"


class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)

    def __repr__(self):
        return f"Availability({self.id})"


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    description = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f"Request({self.id}, {self.name})"


