from CovidHelp import db
import datetime

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(50))
    email = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100))
    link = db.Column(db.String(100))

class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

class Availability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    resource_id = db.Column(db.Integer, db.ForeignKey('resource.id'))
    service_id = db.Column(db.Integer, db.ForeignKey(''))