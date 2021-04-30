from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectMultipleField, widgets, SelectField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length


class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class ResourceForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=50)])
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
    details = StringField('Details', validators=[DataRequired(), Length(min=1, max=200)])
    link = StringField('Link', validators=[Length(min=1, max=100)])
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
    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=100)])
    phone = StringField('Phone Number', validators=[DataRequired(), Length(min=1, max=50)])
    description = StringField('Description', validators=[DataRequired(), Length(min=1, max=200)])
    submit = SubmitField('Submit')


class AdminLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = submit = SubmitField('Login')

