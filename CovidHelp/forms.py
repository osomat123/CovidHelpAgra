from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets, SelectField
from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ResourceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    type = MultiCheckboxField('Type',
                               choices=[('Oxygen', 'Oxygen'),
                                        ('Hospital Beds - With Oxygen', 'Hospital Beds - With Oxygen'),
                                        ('Hospital Beds - Without Oxygen', 'Hospital Beds - Without Oxygen'),
                                        ('Remdesivir', 'Remdesivir'),
                                        ('Medicines', 'Medicines'),
                                        ('Plasma', 'Plasma'),
                                        ('Food', 'Food'),
                                        ('Ambulance', 'Ambulance'),
                                        ('Emergency Services', 'Emergency Services'),
                                        ('Testing', 'Testing'),
                                        ('Home Services', 'Home Services'),
                                        ('Doctor Consultation', 'Doctor Consultation')],
                              validators=[DataRequired()])
    details = StringField('Details', validators=[DataRequired()])
    link = StringField('Link')
    submit = SubmitField('Submit')

class FilterForm(FlaskForm):
    services = SelectField('Filter by:',choices=[('', 'Show all'),
                                                ('Oxygen', 'Oxygen'),
                                                ('Hospital Beds - With Oxygen', 'Hospital Beds - With Oxygen'),
                                                ('Hospital Beds - Without Oxygen', 'Hospital Beds - Without Oxygen'),
                                                ('Remdesivir', 'Remdesivir'),
                                                ('Medicines', 'Medicines'),
                                                ('Plasma', 'Plasma'),
                                                ('Food', 'Food'),
                                                ('Ambulance', 'Ambulance'),
                                                ('Emergency Services', 'Emergency Services'),
                                                ('Testing', 'Testing'),
                                                ('Home Services', 'Home Services'),
                                                ('Doctor Consultation', 'Doctor Consultation')])
    submit = SubmitField('Submit')

class HelpRequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    submit = SubmitField('Submit')
