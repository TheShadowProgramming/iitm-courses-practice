# Installation of flask

- we only have pip command for the installation of the flask project
- so therefore create a virtual environment first then
- install flask there

for venv :- 

run this command in the directory in which we want to install the virtual environment
- python3 -m venv .venv
- . .venv/bin/activate (for activating the virtual environment)
- deactivate karne ke liye, just the deactivate keyword

# Thing about the virtual environment

- virtual environments are created so that projects having different versions of python don't interfere with each other
- like if we do changes in python version then it may break the projects having different versions of python


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
- To make sure to not push the updates to production before turning off the debugger mode
- we can even set environment variables like export FLASK_APP=app.py (in the directory of app.py ofc)
- In this way flask understands by itself, like jo .env file me bhi store kar sakte and like iss tarah se bhi in built package environment variables ko bhi set kar sakte hai

# Jinja2 Template

- In jinja we can write variables inside {{}} and statements like if, for loops and stuff in {%%} blocks 
- and for comments we use this {##}, renaming the template html files into .html.jinja will help the IDEs classify them better 
- every code block has to be mandatorily closed like endif, endfor, endblock etc.

# Template Inheritance and url_for method 

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
- also make sure to use _ instead of hyphens since it is not allowed in naming blocks in jinja template system