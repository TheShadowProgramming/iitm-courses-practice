from flask_wtf import FlaskForm;  # type: ignore
from wtforms import StringField, PasswordField, SubmitField, BooleanField; # type: ignore
from wtforms.validators import Length, DataRequired, Email, EqualTo; # type: ignore

# StringField defines the type of the input, type checking for debugging
# validators make sure that the input follows the rules present inside the array of the validators
# every validator makes sense by themselves so yea
# PasswordField different hai StringField se since password hide wgera karna rehta hai 
# submitField is also different from the passwordField, maybe it'll return  
# EqualTo validator me jo bhi variable pass karenge uske equal hoga apna existing variable

class signupForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=30)])
    confirmPassword = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submitButton = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submitButton = SubmitField('Login')