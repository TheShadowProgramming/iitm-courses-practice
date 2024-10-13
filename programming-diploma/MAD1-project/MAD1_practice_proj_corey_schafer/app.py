from flask import Flask; # type: ignore
# some error with importing flask, will see laterpp
from markupsafe import escape; # type: ignore
from flask import render_template;

app = Flask(__name__);

@app.route("/")
@app.route("/home/<string:name>") # In this way, we can add multiple routes where we want the same function to respond with , <> me string converter hai jiske wajah se the input provided by the user is converted into a string automatically
def hello_world(name): # function ke argument me query parameters of path must be passed
    return f'Hello {escape(name)}'; # making sure that name variable is considered string only, this is automatically done by the jinja2 templating engine

@app.get("/login")
def loginGet():
    return render_template('loginGet.html', person='randomPerson\'s name') # here person is the prop that we're passing in the template