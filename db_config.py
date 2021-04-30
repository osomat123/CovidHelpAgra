from CovidHelp import db, bcrypt
from CovidHelp.models import *

print("Starting DB Configuration...")

try:
	db.create_all()
	print('Schema Setup Complete')
	print()

except Exception as e:
	print('Problem in db.create_all()')
	print(e)
	exit()

try:
	print('Populating Services Table')
	for serv in ['Oxygen','Hospital Beds - With Oxygen', 'Hospital Beds - Without Oxygen', 'Remdesivir', 'Medicines', 'Plasma',  'Food', 'Ambulance', 'Emergency Services', 'Testing', 'Home Services', 'Doctor Consultation']:
		service = Service(name=serv)
		db.session.add(service)
		db.session.commit()
	print('Service Table Population Complete')
	print()

except Exception as e:
	print('Could not populate Services Table')
	print(e)
	exit()

try:
	print('Setting Up Admin')
	username = input('Enter admin username: ')
	password = bcrypt.generate_password_hash(input('Enter Password: ')).decode('utf8')
	admin = Admin(username=username, password=password)
	db.session.add(admin)
	db.session.commit()
	print('Admin Setup Complete')
	print()

except Exception as e:
	print('Could not setup Admin')
	print(e)
	exit()

print('DB Configuration Complete!')
print('You can start the app now')