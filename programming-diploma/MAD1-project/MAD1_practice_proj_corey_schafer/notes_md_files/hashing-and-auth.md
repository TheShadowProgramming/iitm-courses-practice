# For data breach security

- we make sure that the password that we recieve from the users is not stored directly and like we hash the password first and then store it
- once we hash the password then we can check the hashed_password 
- pip install flask-bcrypt
- from flask_bcrypt import Bcrypt class

- bcrypt instance banane ka Bcrypt() class se
- hashed_pw = bcrypt_instance.generate_password_hash('password_in_string_form').decode('urf-8')
- this decode('utf-8') method makes the hashed_pw in the form of string of 'utf-8'   

- and then we store the hashed_pw in the database 
- also everytime, you run the generate_password_hash() method, then everytime you'll get different hashed_pw which makes it secure and safe to use

- in order the check whether the user gave correct password or not, we can use the method 

bcrypt.check_password_hash(hashed_pw, 'password_entered_by_the_user')

- now like the variable hashed_pw was originally generated when the user gave the password during signup, and now we check hashed_pw with the password that the user gives during the login

# Under the hood of hashing and salting in the Bcrypt

- in the bcrypt instance, the check_password_hash() checks the given password by the user with the hashed_pw by using the salt and the Cost Factor present in the hashed_pw and then hashes the password again given by the user and checks whether the two passwords are equal or not 
