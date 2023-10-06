from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DateTimeLocalField, IntegerField
from wtforms.validators import DataRequired

class login_form(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()]
    phone_number = StringField("Phone number", validators=[DataRequired(), Length(min=10, max=10), Regexp(^[0-9]+$)]
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
