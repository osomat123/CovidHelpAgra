from flask import render_template, url_for,redirect, request
from CovidHelp import app, db
from CovidHelp.forms import *
from CovidHelp.models import *

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ResourceForm', methods=['GET', 'POST'])
def resource_form():
    form = ResourceForm()

    if form.validate_on_submit():
        return 'Yayyyyy!!!'
    return render_template('form.html', form=form)