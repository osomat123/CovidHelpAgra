from flask import render_template, url_for,redirect, request, flash, jsonify
from CovidHelp import app, db
from CovidHelp.forms import *
from CovidHelp.models import *

@app.route('/', methods=['GET','POST'])
def home():
    data = []
    form = FilterForm()
    resources = []
    if(form.validate_on_submit()):
        print(form.services.data)
        if form.services.data:
            service_id = Service.query.filter_by(name=form.services.data).first().id
            availability = Availability.query.filter_by(service_id=service_id).all()
            for item in availability:
                resources.append(Resource.query.filter_by(id=item.resource_id).first())

            print(availability)
            print(resources)

    if not resources:
        resources = Resource.query.order_by(Resource.upvotes).all()

    resources.reverse()
    for resource in resources:
        availability = Availability.query.filter_by(resource_id=resource.id).all()
        services = []
        for item in availability:
            services.append(Service.query.filter_by(id=item.service_id).first())


        data.append((resource, services))

    return render_template('home.html', data=data, form=form)

@app.route('/upvoteResource', methods=['POST'])
def upvote_resource():
    resource_id = int(request.form['id'])
    upvote_amount = int(request.form['amount'])
    resource = Resource.query.filter_by(id=resource_id).first()
    resource.upvotes += upvote_amount

    db.session.add(resource)
    db.session.commit()

    return jsonify({'upvotes': resource.upvotes})

@app.route('/ResourceForm/', methods=['GET', 'POST'])
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

@app.route('/HelpRequests/', methods=['GET', 'POST'])
def help_Requests():
    data = []
    request = []
    form = HelpRequestForm()

    if(form.validate_on_submit):
        print(form.name.data)
    return render_template('help-request.html',data=data, form=form)

@app.route('/NewRequest/', methods=['GET', 'POST'])
def request_form():
    form = HelpRequestForm()
    return render_template('new-request.html', form=form)