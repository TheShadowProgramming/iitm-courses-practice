# WTForms Installation

- we gotta install the WTForms package in the virtual environment itself and make sure to use the flag when the installation is not happening properly

- pip install flask-wtf --break-system-packages (in this way it gives some permission which I Don't know for now)

- pip install -U FLask-WTF --break-system-packages (this is the command to install the Flask_WTF integration)

# Basic Syntax 

- It is present in the forms.py file and like remember that Flask_wtf ka syntax is different than the wtforms ka syntax and we're using the flask_wtf syntax

- One thing to remember is that even though the wtforms syntax follows a class syntax with the input fields being the class specific variables, these variables become specific to the instances of the classes too when we create instance/form of these classess

- we maintain secret keys too to make sure that security of the form is not compromised
- like cross-site request forgery, it is a method where attacker sends some html and js which will unintentionally send requests to your logged in websites and make some unintentional changes to the websites in which you've alredy logged in
- so maintaining secret keys will make sure that the key is stored in the server and server sends signed cookies only which makes sure that the cookies are not tampered by the client side from the attackers

# Secret_Key generation

- python3 in the CLI, then importing secrets module of the python package, then secrets.token_hex(16) to get a token of 16 characters
