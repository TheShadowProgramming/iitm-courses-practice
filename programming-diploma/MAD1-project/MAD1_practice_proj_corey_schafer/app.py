from flask import Flask; # type: ignore
# some error with importing flask, will see later
from markupsafe import escape; # type: ignore
from flask import render_template;
from forms import RegistrationForm, LoginForm;

app = Flask(__name__);

# App.config se we access the environment variables

app.config['DEBUG'] = True;
app.config['SECRET_KEY'] = '75b7604b399240a54b9c44c51868ff34';

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'October 20 2024'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'October 21 2024',
    }
]


@app.route("/")
def home():
    return render_template('home.html', title='Home') # here title is the prop that we're passing in the template

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    return render_template('signup.html', title="SignUp", form=form)


@app.route("/checking-escape/<string:name>") # In this way, we can add multiple routes where we want the same function to respond with , <> me string converter hai jiske wajah se the input provided by the user is converted into a string automatically
def hello_world(name): # function ke argument me query parameters of path must be passed
    return f'Hello {escape(name)}'; # making sure that name variable is considered string only, this is automatically done by the jinja2 templating engine

if __name__ == "__main__":
    app.run()