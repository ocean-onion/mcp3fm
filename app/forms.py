from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    """Form for users to create new account"""
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        """Username must be unique"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        """Email must be unique"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    """Form for users to login"""
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PluginUploadForm(FlaskForm):
    """Form for users to upload a plugin file"""
    plugin_file = FileField('Plugin File', validators=[DataRequired()])
    submit = SubmitField('Upload')

class CustomizationForm(FlaskForm):
    """Form for users to input customization options for plugins/mods"""
    customization_options = TextAreaField('Customization Options', validators=[DataRequired()])
    submit = SubmitField('Customize')

class RatingForm(FlaskForm):
    """Form for users to rate a plugin or mod"""
    rating = StringField('Rating', validators=[DataRequired()])
    submit = SubmitField('Rate')
