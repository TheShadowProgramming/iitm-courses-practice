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

# cookies Intro and some more terminologies 

- so cookies are text file that browser stores for different different websites
- it acts like a memory card for the websites, 

document.cookie = "username=dean, expiry=some_utc_format_date_and_time, path=some_route_at_which_the_website_can_access_the_cookie_stored"

### 3 types of cookies :-

1. session cookies

- ye cookie sirf browser chaalu rehne tak tikta hai, browser band hone ke baad cookie automatically delete ho jaata hai 

2. permanent cookies

- ye cookies lamba tikte hai and browser band hone ke baad bhi tikte hai 

3. Third-party cookies

- ye cookies install hote hai marketing websites ke dwara to track the internet behaviour of the user and then they use the data to give us targeted marketing ads

### Session module in flask

- flask has one module session which is used by this flask-login package under the hood to make sure that user logs in again without entering the email and password again
- sessions module stores cookies and signs it cryptographically in the user's browser storage, and it means that the user can view the cookie but can't modify it until and unless they have the secret_key by which the cookie was signed cryptograhically 

### Request module in flask 

- just like the sessions module, request module helps in extracting the cookie stored in the user's browser that user sends while hitting the request to the server
- and the backend dev can access the cookie that the user is passing using the attributes of the request object like request.form, request.method, request.args to access the arguments passed through the url of the request, request.json to access the json data sent through the requests like POST, PUT and stuff, request.headers to access the headers of the request
- request.cookies to access the cookies present for the route, request.files to access the files uploaded by the user, 

- request.args is dictionary which has keys equal to the query parameters passed and the value of the keys being the value of the query parameter

- if we try to access some query parameter which doesn't exists with the help of the dot notation or the square bracket notation then it may throw an error 

- and thus these type of modules usually have a .get() method which gives us none if the query parameter doesn't exists, which we can use to make sure that the website doesn't throw an error when the query parameter doesn't exists

# Login memory, authentication using tokens
- for user memory and login and logout logic, we use the package flask-login
- the package does the session and request interaction for us under the hood and we don't need to do anything
- pip install flask-login   
- from flask_login import LoginManager() class
- the instance created from the LoginManager needs initialization
login_manager.init_app(app)
- and the instance has many methods like the @load_user decorator ke baad we create a function load_user() which retrieves the user jiska id you have stored in the session cookie ki haa bhai ye id logged in hai to uska id leke database me query ho jaati hai 
- remember_me field me jo data aayega usse we can make sure that this id is not only stored in the session cookie but also in the permanent cookie, that happens in the login_user() type of function usme we pass the value of the remember property
- modifying this cookie is not possible since the cookie is signed and in order to modify it you need a secret_key which is present in our project's environment variables
- we can protect some routes by making sure that the person logs in before accessing that route by using the @login_required decorator

# Methods and variables from flask-login package

- we have login_user, logout_user methods 
- and variables like the current_user which has the attribute is_authenticated
- and this is happening since we passed the UserMixin class which made sure that the user object has these methods whether the user is_active, is_authenticated
- current_user is the user retrieved from the database using the load_user decorator function
- login_required decorator redirects the user to the login route, but we gotta define the login route in the init file, the value of the login_view is the name of the function which represents the login route
- there is another attribute named the login_message_category in the login_manager instance which we can set to a bootstrap class since we give the category of the flash message as the boostrap class only in our project

- once we try to access the account page when not logged in then the login_required decorator redirects the user to the login page and also gives the page's name from where the user was redirected to the login page, we can access that name of the route to make sure that after login the user is redirected to same route from where it came from