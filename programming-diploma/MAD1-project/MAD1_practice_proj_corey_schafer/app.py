from flask import Flask; # type: ignore
# some error with importing flask, will see later
from markupsafe import escape; # type: ignore
from flask import render_template, url_for;

app = Flask(__name__);


@app.get("/")
def home():
    return render_template('jinja-templates/components/home.html', title='home') # here title is the prop that we're passing in the template

@app.route("/checking-escape/<string:name>") # In this way, we can add multiple routes where we want the same function to respond with , <> me string converter hai jiske wajah se the input provided by the user is converted into a string automatically
def hello_world(name): # function ke argument me query parameters of path must be passed
    return f'Hello {escape(name)}'; # making sure that name variable is considered string only, this is automatically done by the jinja2 templating engine
