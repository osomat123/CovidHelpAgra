from flask import render_template, url_for,redirect, request
from CovidHelp import app, db

@app.route('/')
def home():
    return render_template('index.html')