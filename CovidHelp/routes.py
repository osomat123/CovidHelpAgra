from flask import render_template, url_for,redirect, request, flash
from CovidHelp import app, db
from CovidHelp.forms import *
from CovidHelp.models import *

@app.route('/')
def home():
    data = []

    resources = Resource.query.all()
    for resource in resources:
        availability = Availability.query.filter_by(resource_id=resource.id).all()
        services = []
        for item in availability:
            services.append(Service.query.filter_by(id=item.service_id))

        data.append((resource, services))

    return render_template('home.html', data=data)

@app.route('/upvotePost/<int:post_id>', methods=['POST'])
def upvote_post():
    pass

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