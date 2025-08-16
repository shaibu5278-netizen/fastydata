from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,SelectField
from wtforms.validators import DataRequired,Length,EqualTo,ValidationError,Email,Optional

class RegisterationForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=80)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=80)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email', validators=[Optional(), Email()])
    phone_number = StringField('Phone Number', validators=[Optional(), Length(max=15)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class EditUserForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(), Length(min=1, max=80)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(min=1, max=80)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=80)])
    email = StringField('Email', validators=[Optional(), Email()])
    phone_number = StringField('Phone Number', validators=[Optional(), Length(max=15)])
    user_type = SelectField('User Type', choices=[('user', 'User'), ('admin', 'Admin')], validators=[DataRequired()])
    password = PasswordField('New Password (leave blank to keep current)')
    submit = SubmitField('Update')
