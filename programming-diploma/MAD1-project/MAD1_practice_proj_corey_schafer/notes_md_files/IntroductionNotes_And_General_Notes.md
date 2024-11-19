# Installation of flask

- we only have pip command for the installation of the flask project
- so therefore create a virtual environment first then
- install flask there

for venv :- 

run this command in the directory in which we want to install the virtual environment
- pip install virtualenv (virtual env create karne ke liye package)
- python3 -m virtualenv .venv/any_other_folder_name_of_the_virtual_env
- . name_of_the_virtual_env_folder_created/bin/activate (for activating the virtual environment)
- deactivate karne ke liye, just the deactivate keyword

# Thing about the virtual environment

- virtual environments are created so that projects having different versions of python don't interfere with each other
- like if we do changes in python version then it may break the projects having different versions of python

# Decorator functions 

- decorator functions are defined in a way to make sure that they accept the function as an input over which they are called using the @ syntax
- and then function defined inside the decorator runs whenever we call the outer function over which the decorater is defined

def decorator_function(function):
    def function2:
        return (var2 + function())
    
    return function2

@decorator_function
def function1():
    return var1

function1() # supposed output is var1 and var2

- common use case is when we want to add some common change to all the functions present in the application then we can use the decorator which modifies the original function consistently

# Class based approach of the flask application
- we create application using Flask Class only
- now the thing is we pass __name__ variable in the class which is a inbuilt-variable in python which stores the value of the status of the of the current file in execution flow 
- like if we use __name__ in a file and run that file then it means that we're considering that file as main file therefore the variable will store value __main__ in it since we ran the file as the first thing in our execution flow
- if we import that file in some other module and run that other module then the code present in our file will be imported in the module and therefore we use the functions in the files so that we can decide even after importing the code ki when to run it under certain condition
- if we import that file in some other module to fir usse __name__ takes value as the name of the file jisko we imported since we're running the module and not the other file and therefore the status of the file is not main anymore
- we pass this __name__ variable in the flask while creating an instance of the app through this flask knows where to access some other data from for seamless execution of the application

# Running the flask application and to enter the debug mode

- flask --app "name-of-the-flask-app" run
- to enter debug mode we use this command "flask --app hello run --debug" [hello ke jagah pe you use the name of the flask app file]
- or even we can make environment variables which will store the info whether to enter the debug mode or not while running the server, this method is prefered since the debugger mode/development mode allows the user to manipulate the code from the browser itself 
- if we want to modify the code from the browser itself then we can use the debugger pin present in the terminal and enter that pin in the browser to change the code from the browser itself
- To make sure to not push the updates to production before turning off the debugger mode
- we can even set environment variables like export FLASK_APP=app.py (in the directory of app.py ofc)
- In this way flask understands by itself, like jo .env file me bhi store kar sakte and like iss tarah se bhi in built package environment variables ko bhi set kar sakte hai

# Jinja2 Template

- In jinja we can write variables inside {{}} and statements like if, for loops and stuff in {%%} blocks 
- and for comments we use this {##}, renaming the template html files into .html.jinja will help the IDEs classify them better 
- when we're returning some template under some route in the main app.py file then the template need not to remain in the root location of the templates directory, it can also stay in the nested folder structures too 
- every code block has to be mandatorily closed like endif, endfor, endblock etc.

# Template Inheritance and url_for method 

- url_for method me simply first arguement daalo the folder and then the file name ko cater karne wala view function like the function which returns the template that you want to render on the screen (automatically vo url generate kar dega), and also this method is specific to flask so we have use jinja syntax for using this method
- So like yea flask or jinja is not like react where we're having single page website and then everything is getting manipulated using virtual DOM and stuff
- In flask like frameworks we send separate html files for every request and path that exists on the website, and as a result we have to write the html boilerplate code everytime we create some new jinja template
- Now the thing is we can create some layouts and then use "block" keywords where new code will be added when we write "extends name_of_parent.html" at the top of our child html file 

# Static folder and stuff + Template Inheritance

- we should include all the css and js files in static folder by default since that is the structure of the 
- Through Template Inheritance we can bring the similar effects that classes and objects have in progamming 
- Sort of OOP type approach in frontEnd
- We're using bootstrap to style our website which is developed using flask, and we'll use cdn to link our css files
- So like cdn which is content delivery network which hosts remote files on their server and when we link these files directly in our html file then our html files extracts the styles and remote js from the server
- So like there's a drawback to this approach since we're depending on some external package for our code
- also make sure to use _ instead of hyphens since it is not allowed in naming blocks in jinja template system, using hyphens in the attributes passed through the wt_Forms package is also not allowed in jinja template system 
- form.csrf_token is more specific that it'll send only the csrf_token and the form.hidden_tag will send the entire hidden info of the request
- Remember that the CSRF token is generated at the moment when the page loads for which we included a form.hidden_Tag, generation of this token is dependant on the secret_key passed in the app.py file and when the malicious user sends the request to the route for which the CSRF token is required, backend responds with a bad request 
- and then the CSRF token passed with the form is authenticated with the CSRF token generated in the backend for the form 
- url_for method generates the url for the function serving the different routes that we build for the web app like it doesn't builds the routes for the template files, this is true for the regular route functions in the root directory
- but for accessing the files inside the static folder we actually pass the file name using the filename attribute of the url_for method

# Flask redirection and other special methods

- redirect method me insert the url_for method by generating the location of the file and obviously this function makes sure any code written below it doesn't runs 
- flash message used in the redirection process stores the message that has passed into it in the first argument and also stores some meta data about the flash message in the 2nd argument named category, and also the main function of the flash message is that the flash message will only store the data until the next request to the same route for which the flash message has been defined upon
- since the flash message works between requests and uses sessions module under the hood, therefore we need secret_key to make sure that user doesn't plays with the session
- and remember flash message has to be retrieved in the template where we want the flash message, and flash message stores the info until the next request from the user is not sent to any route of the web app 
- form.anyField.data gives the data given by the user
- the submitField created using the wt_forms package runs the view function's code again when the user presses the button

# Flask Components and macros, and re-renders of the templates

- we can use {% include 'path/filename.html' %} to include other components/macros in flask just like react and it works just like react like then html inside the filename.html it directly rendered wherever we call the {% include part %}
- this include syntax doesn't support the props syntax so we use the macros syntax to pass props along with rendering the templates, so to like create a re-usable template or component
- jinja templates are executed on the server side and then sent to the client requesting the html file, so the template code only runs whenever the user does the request again to the same route 