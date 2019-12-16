from flask import Flask
from BugTracker.config import Config  
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config.from_object(Config)

mongo = PyMongo(app)
#bcrypt =Bcrypt(app)

from BugTracker.users.routes import users
from BugTracker.main.routes import main
from BugTracker.bugs.routes import bugs

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(bugs)


