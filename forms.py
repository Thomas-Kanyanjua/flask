from flask_wtf import FlaskForm
from wtforms import EmailField,SubmitField,StringField,PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo

class RegistrationForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired(),Length(min=2,max=15),])
    email=EmailField('Enter Email',validators=[DataRequired(),Email(),])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8,max=16),])
    confirm_password=PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign up')

class LoginForm(FlaskForm):
    
    email=StringField('Enter Email',validators=[DataRequired(),Email(),])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=8,max=16),])
    remember_me=BooleanField('Remember Me?')
    submit=SubmitField('Log in',validators=[])
    