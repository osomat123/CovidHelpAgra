from CovidHelp import db
import datetime

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    details = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(100))
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
