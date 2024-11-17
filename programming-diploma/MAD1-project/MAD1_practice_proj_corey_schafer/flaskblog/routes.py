from flask import render_template, redirect, url_for, flash; # type: ignore
from flaskblog.forms import signupForm, LoginForm;
from flaskblog.models import User, Post;
from flaskblog import app, db, flask_bcrypt;

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
    return render_template('routes/home.html', title='Home', posts=posts) # here title is the prop that we're passing in the template

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "monishmishra966@gmail.com" and form.password.data == "Monmis@230903":
            flash("You're logged in as an admin", 'success')
            return redirect(url_for('home'))
        else:
            # handle error logic in else and logging in of other accounts in elif here 
            flash("You're not logged in as an admin", 'danger') # remove this once we connect database to the application
    return render_template('routes/login.html', title="Login", form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = signupForm()
    if form.validate_on_submit():

        hashed_pw = flask_bcrypt.generate_password_hash(form.password.data).decode('utf-8'); # we can even directly pass the function in the password of the new_user without creating the variable here

        new_user = User(username=form.username.data, email=form.email.data, password=hashed_pw)

        db.session.add(new_user)
        db.session.commit()

        flash(f'Successfully created a user, now you can login in', 'success')
        return redirect(url_for('login'))
    
    return render_template('routes/signup.html', title="SignUp", form=form) # iss tarah se render_template method me first argument me folder ke naam ke saath file name dena padega

@app.route('/about', methods=['GET'])
def about():
    return render_template('routes/about.html')


# @app.route("/checking-escape/<string:name>") # In this way, we can add multiple routes where we want the same function to respond with , <> me string converter hai jiske wajah se the input provided by the user is converted into a string automatically
# def hello_world(name): # function ke argument me query parameters of path must be passed
#     return f'Hello {escape(name)}'; # making sure that name variable is considered string only, this is automatically done by the jinja2 templating engine

