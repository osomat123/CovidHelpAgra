from CovidHelp import db
from CovidHelp.models import *

db.create_all()
for serv in ['Oxygen','Hospital Beds - With Oxygen', 'Hospital Beds - Without Oxygen', 'Remdesivir', 'Medicines', 
	     'Plasma',  'Food', 'Ambulance', 'Emergency Services', 'Testing', 'Home Services', 'Doctor Consultation']:
	service = Service(name=serv)
	db.session.add(service)
	db.session.commit()
