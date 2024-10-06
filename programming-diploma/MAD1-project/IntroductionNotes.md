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

# FLask's url re-direction behavior

- so like flask has a mechanism of redirecting simlar urls to their proper places so that browsers don't consider these different urls as different pages which decreases the SEO of these pages
- project like url ko '/project/' bana deta and file like url ko normal 'file/' type url bana deta