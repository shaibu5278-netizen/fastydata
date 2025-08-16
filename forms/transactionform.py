from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SelectField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, NumberRange, Regexp

class TransactionForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    transaction_type = SelectField('Type', choices=[('credit', 'Credit'), ('debit', 'Debit')], validators=[DataRequired()])
    payment_type = SelectField('Payment Type', coerce=int, validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(max=255)])
    submit = SubmitField('Add Transaction') 