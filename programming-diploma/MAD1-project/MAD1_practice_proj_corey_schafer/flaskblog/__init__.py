from flask import Flask;
# some error with importing flask, will see later
# from markupsafe import escape; # type: ignore
from flask_restful import Resource, api; # type: ignore
from flask_sqlalchemy import SQLAlchemy # type: ignore
from flask_bcrypt import Bcrypt; # type: ignore
from flask_login import LoginManager; # type: ignore

app = Flask(__name__, template_folder='./templates', static_folder='./static')

# App.config se we access the environment variables

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = '75b7604b399240a54b9c44c51868ff34';

db = SQLAlchemy(app);

flask_bcrypt_instance = Bcrypt(app);  

login_manager = LoginManager();
login_manager.init_app(app);
login_manager.login_view = 'login';
login_manager.login_message_category = 'info'

from flaskblog import routes;