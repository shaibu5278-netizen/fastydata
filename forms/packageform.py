from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, TextAreaField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Optional, NumberRange, URL
from flask_wtf.file import FileField, FileAllowed

class PackageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[Length(max=255)])
    image = FileField('Image', validators=[Optional(), FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Images only!')])
    is_active = BooleanField('Active')
    submit = SubmitField('Save')

class PackageItemForm(FlaskForm):
    package_id = SelectField('Package', coerce=int, validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    price = FloatField('Price', validators=[DataRequired(), NumberRange(min=0, message='Price must be positive')])
    is_active = BooleanField('Active', default=True)
    submit = SubmitField('Save') 