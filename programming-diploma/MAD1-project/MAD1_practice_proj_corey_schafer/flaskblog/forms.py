from flask_wtf import FlaskForm;  # type: ignore
from flask_wtf.file import FileField, FileAllowed; # type: ignore
from flask_login import current_user; # type: ignore
from wtforms import StringField, PasswordField, SubmitField, BooleanField; # type: ignore
from wtforms.validators import Length, DataRequired, Email, EqualTo, ValidationError; # type: ignore
from flaskblog.models import User;

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

    def validate_username(self, username):
        
        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('User with the given username already exists')
    
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('User with the given email already exists')
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberMe = BooleanField('Remember Me')
    submitButton = SubmitField('Login')  

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()

        if not user:
            raise ValidationError("This email doesn't exists, please signup")
        
class AccountUpdateForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture_file = FileField("Update Profile Picture", validators=[FileAllowed(['jpg', 'png'])])
    submitButton = SubmitField('Update')

    def validate_username(self, username):
        if current_user.username != username.data: # if user gives the same username and email as update then it would throw an error, so we gotta check it first
            user = User.query.filter_by(username=username.data).first()

            if user:
                raise ValidationError('User with the given username already exists')
    
    def validate_email(self, email):
        if current_user.email != email.data:
            user = User.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('User with the given email already exists')