# WTForms Installation

- we gotta install the WTForms package in the virtual environment itself and make sure to use the flag when the installation is not happening properly

- pip install flask-wtf --break-system-packages (in this way it gives some permission which I Don't know for now)

- pip install -U FLask-WTF --break-system-packages (this is the command to install the Flask_WTF integration)

- pip install email_validator --break-system-packages (this command to install the email_validator package used for the email_validator function under the hood for the Email())

# Basic Syntax 

- It is present in the forms.py file and like remember that Flask_wtf ka syntax is different than the wtforms ka syntax and we're using the flask_wtf syntax

- One thing to remember is that even though the wtforms syntax follows a class syntax with the input fields being the class specific variables, these variables become specific to the instances of the classes too when we create instance/form of these classess

- we maintain secret keys too to make sure that security of the form is not compromised
- like cross-site request forgery, it is a method where attacker sends some html and js which will unintentionally send requests to your logged in websites and make some unintentional changes to the websites in which you've alredy logged in
- so maintaining secret keys will make sure that the key is stored in the server and server sends signed cookies only which makes sure that the cookies are not tampered by the client side from the attackers

# Secret_Key generation

- python3 in the CLI, then importing secrets module of the python package, then secrets.token_hex(16) to get a token of 16 characters

# Error handling in the wt_Forms 

- so like whenever user inputs the forms with some credentials then the form may throw some error which we can access using the form.form_component.errors attribute and then we can loop over it and make the form component have the style that the user has done some error by using the is-invalid bootstrap class

# Custom validation of the forms 

- so we can introduce custom validation for our form fields too, use cases are like whether the user is already logged in or not
- we can check whether the data entered by the user is already present in the database or not and then accordingly pass the validtion or not 
- if we raise ValidationError('custom_message_here'), where the ValidationError() method is one of the validators of the wtforms package, makes sense why is it a validator
- then the error message that we passed in the ValidationError() method is dealt with in the signup.html and login.html jaha pe we have made custom bootstrap elements for handling this

- so the validate_on_submit() method invokes all the validator methods present in the flask Form
- and also invokes the function of the format validate_<field_name>(self, <field_name>) which we define inside the class, like we don't need to call it seperately, flask-wtf calls the methods of these formats by itself when we call the validate_on_submit()
