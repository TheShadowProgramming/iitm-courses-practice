from flask import Flask;
# some error with importing flask, will see later
# from markupsafe import escape; # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore

app = Flask(__name__, template_folder='../templates', static_folder='../static', )

# App.config se we access the environment variables

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['DEBUG'] = True;
app.config['SECRET_KEY'] = '75b7604b399240a54b9c44c51868ff34';

db = SQLAlchemy(app)

from flaskblog import routes;
from flask_bcrypt import Bcrypt; # type: ignore

flask_bcrypt = Bcrypt(app);