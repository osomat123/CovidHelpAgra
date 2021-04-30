from flask import render_template, url_for,redirect, request, flash, jsonify
from CovidHelp import app, db, bcrypt, login_manager
from flask_login import login_user, logout_user, login_required, current_user
from CovidHelp.forms import *
from CovidHelp.models import *


@app.route('/', methods=['GET','POST'])
def home():
    data = []
    form = FilterForm()
    resources = []
    if(form.validate_on_submit()):
        if form.services.data:
            service_id = Service.query.filter_by(name=form.services.data).first().id
            availability = Availability.query.filter_by(service_id=service_id).all()
            for item in availability:
                resources.append(Resource.query.filter_by(id=item.resource_id).first())

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

        flash("Resource Added Successfully", 'alert alert-success')
        return redirect(url_for('home'))

    return render_template('new-resource-form.html', form=form)


@app.route('/RequestForm/', methods=['GET', 'POST'])
def request_form():
    form = HelpRequestForm()

    if form.validate_on_submit():
        request = Request(name=form.name.data,
                          phone=form.phone.data,
                          description=form.description.data)

        db.session.add(request)
        db.session.commit()
        flash("Request Added Successfully", 'alert alert-success')
        return redirect(url_for('help_requests'))

    return render_template('new-request-form.html', form=form)


@app.route('/HelpRequests/')
def help_requests():
    requests = Request.query.all()
    return render_template('requests.html', requests=requests)

# Admin Login Related Code


@app.route('/AdminDashboard/')
@login_required
def admin_dashboard():
    return render_template('admin-dashboard.html')


@app.route('/AdminLogin/', methods=['GET', 'POST'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('admin_dashboard'))

    form = AdminLoginForm()

    if form.validate_on_submit():
        user = Admin.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('admin_dashboard'))

        else:
                flash("Incorrect username or password", 'alert alert-danger')

    return render_template('admin-login-form.html', form=form)

@login_required
@app.route("/AdminLogout/")
def logout():
    logout_user()
    return redirect(url_for('home'))