from flask import render_template, url_for,redirect, request, flash
from CovidHelp import app, db
from CovidHelp.forms import *
from CovidHelp.models import *

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ResourceForm', methods=['GET', 'POST'])
def resource_form():
    form = ResourceForm()

    if form.validate_on_submit():

        resource = Resource(name=form.name.data,
                            phone=form.phone.data,
                            details=form.details.data,
                            link=form.link.data)
        db.session.add(resource)
        db.session.commit()
        
        for service_type in form.type.data:
            service = Service.query.filter_by(name=service_type).first()
            avail = Availability(resource_id=resource.id, service_id=service.id)
            db.session.add(avail)
            db.session.commit()

        flash("Resource Added Successfully", 'flash_success')
        return redirect(url_for('home'))

    else:
        flash("Please fill the form correctly", 'flash_fail')
    return render_template('form.html', form=form)