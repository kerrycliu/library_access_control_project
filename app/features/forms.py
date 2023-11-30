from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, HiddenField, SelectField, PasswordField, BooleanField, SubmitField, TextAreaField, DateTimeLocalField, IntegerField
from wtforms.validators import DataRequired,Length,Regexp
import re

class login_form(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    guest = HiddenField('Guest')
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class sign_up_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    role = SelectField('Role', choices=[('user', 'User'), ('librarian', 'Librarian'), ('admin','Administrator'), ('guest', 'Guest')], validators=[DataRequired()])
    # Role selection TODO: Check, might not be right format
    #permission_user = BooleanField("User")
    #permission_librarian = BooleanField("Librarian")
    #permission_admin = BooleanField("Administrator")
    #permission_guest = BooleanField("Guest")
    submit = SubmitField('Sign Up')

class checkout_book_form(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    book_title = StringField('Book Title', validators=[DataRequired()])
    submit = SubmitField('Checkout')

class edit_profile_form(FlaskForm):
    new_username = StringField('Username', validators=[DataRequired()])
    new_password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Edit')

class add_books_to_library(FlaskForm):
    book_name = StringField('Book Title', validators=[DataRequired()])
    book_genere = StringField('Book Genere', validators=[DataRequired()])
    book_available = BooleanField('Available')
    submit = SubmitField('Add')

class delete_user_form(FlaskForm):
    username_del = StringField('Username', validators=[DataRequired()])
    admin_cred = StringField('Admin Username', validators=[DataRequired()])
    reason_del = TextAreaField('Reason for Deletion', validators=[DataRequired()])
    submit = SubmitField('Delete')
