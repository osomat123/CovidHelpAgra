from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
import email_validator

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class ResourceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email()])
    type = MultiCheckboxField('Type',
                               choices=[(1, 'Oxygen'),
                                        (2, 'Hospital Beds - With Oxygen'),
                                        (3, 'Hospital Beds - Without Oxygen'),
                                        (4, 'Remdesivir'),
                                        (5, 'Medicines'),
                                        (6, 'Plasma'),
                                        (7, 'Food'),
                                        (8, 'Ambulance'),
                                        (9, 'Emergency Services'),
                                        (10, 'Testing'),
                                        (11, 'Home Services'),
                                        (12, 'Doctor Consultation')],
                               validators=[DataRequired()])
    details = StringField('Details', validators=[DataRequired()])
    link = StringField('Link')
    submit = SubmitField('Submit')


