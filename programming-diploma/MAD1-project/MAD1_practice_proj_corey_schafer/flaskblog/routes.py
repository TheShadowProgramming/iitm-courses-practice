import secrets;
import os;
from PIL import Image; # type: ignore
from flask import render_template, redirect, url_for, flash, request; # type: ignore
from flaskblog.forms import signupForm, LoginForm, AccountUpdateForm, PostForm;
from flaskblog.models import User, Post;
from flaskblog import app, db, flask_bcrypt_instance;
from flask_login import login_user, logout_user, current_user, login_required; # type: ignore

@app.route("/")
def home():
    posts = Post.query.all();
    return render_template('routes/home.html', title='Home', posts=posts, current_user=current_user) # here title is the prop that we're passing in the template

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    admin_user = User.query.get(1);

    if form.validate_on_submit() and form.email.data == admin_user.email and flask_bcrypt_instance.check_password_hash(admin_user.hashed_password, form.password.data):
        login_user(admin_user, remember=form.rememberMe.data)
        flash("You've successfully logged in as an admin", 'success')
        return redirect(url_for('home'))

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if flask_bcrypt_instance.check_password_hash(user.hashed_password, form.password.data):
            login_user(user, remember=form.rememberMe.data)
            flash(f"You're logged in with the email :- {form.email.data}", 'success')
            next_page = request.args.get('next')

            return redirect(url_for(next_page[1:])) if next_page else redirect(url_for('home')) 
        else:
            flash("Incorrect password and email combination", 'danger') # remove this once we connect database to the application        
    return render_template('routes/login.html', title="Login", form=form, current_user=current_user)

@app.route("/signup", methods=['GET', 'POST'])
def signup():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = signupForm()
    if form.validate_on_submit():

        hashed_pw = flask_bcrypt_instance.generate_password_hash(form.password.data).decode('utf-8'); # we can even directly pass the function in the password of the new_user without user_idcreating the variable here

        new_user = User(username=form.username.data, email=form.email.data, hashed_password=hashed_pw, password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash(f'Successfully created a user with the email :- {form.email.data}', 'success')
        return redirect(url_for('login'))
    
    return render_template('routes/signup.html', title="SignUp", form=form, current_user=current_user) # iss tarah se render_template method me first argument me folder ke naam ke saath file name dena padega

@app.route('/about', methods=['GET'])
def about_us():
    return render_template('routes/about.html', title="About", current_user=current_user)


@app.route('/logout', methods=['GET'])
def logout():
    logout_user() # don't need to pass anything in the logout_user function just the current user gets logged out by clearing the cookies present in the user's browser 
    return redirect(url_for('home'))

def save_picture_and_return_picture_file_name(picture_file):
    picture_file_extension = os.path.splitext(picture_file.filename)[1]; # this method splitext helps in seperating the file extension, where the first part is the name of the file
    random_hex_code_for_picture_filename = secrets.token_hex(8); # this variable name will be stored in the database instead of the file_name given by the user to avoid duplication and malware integration in the database
    new_hex_code_filename = random_hex_code_for_picture_filename + picture_file_extension
    picture_file_path_to_save_it = os.path.join(app.root_path, 'static/profile_pictures', new_hex_code_filename)

    output_size = (80, 96)
    i = Image.open(picture_file)
    i.thumbnail(output_size)

    i.save(picture_file_path_to_save_it)

    return new_hex_code_filename;
    # TL;DR :- we gave random hex code name to the file and saved it using the FileField data that we got  

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = AccountUpdateForm();

    if form.validate_on_submit():
        if form.picture_file.data:
            
            picture_fn = save_picture_and_return_picture_file_name(form.picture_file.data);

            current_user.image_file_name = picture_fn;
        
        current_user.email = form.email.data;
        current_user.username = form.username.data;
        db.session.commit()
        flash('Account Info has been updated', 'info')
        return redirect(url_for('account')) # once the form is submitted through POST request then we need to make sure that the latest request becomes GET, therefore we deliberately shift the user to the same route with GET request with another request so as to change the state variables, or else when the user refreshes then the POST request is sent to the same route which duplicates the content
    
    elif request.method == 'GET': # when the user doesn't presses update button then the validate_on_submit() method is not invoked since it only invoked for POST request, and then for GET request we make sure that fields populate themselves with the current value by default
        form.email.data = current_user.email
        form.username.data = current_user.username

    image_file_path = url_for('static', filename=f'profile_pictures/{current_user.image_file_name}')
    return render_template('routes/account.html', title="My Account", current_user=current_user, image_file_path=image_file_path, form=form)


@app.route('/post/new', methods=['GET', 'POST'])
@login_required
def post():

    form = PostForm()
    if form.validate_on_submit():

        post_title = form.post_title.data;
        post_content = form.post_content.data;

        post = Post(post_title=post_title, post_content=post_content, user_id=current_user.id)

        db.session.add(post)
        db.session.commit()

        flash('Your Post has been created', 'info')
        return redirect(url_for('home'))
    return render_template('routes/post.html', title='New Post', current_user=current_user, form=form)

@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def update_post():
    return render_template('routes/update_post.html', title='Update Post')

# @app.route("/checking-escape/<string:name>") # In this way, we can add multiple routes where we want the same function to respond with , <> me string converter hai jiske wajah se the input provided by the user is converted into a string automatically
# def hello_world(name): # function ke argument me query parameters of path must be passed
#     return f'Hello {escape(name)}'; # making sure that name variable is considered string only, this is automatically done by the jinja2 templating engine