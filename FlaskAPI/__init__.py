from flask import Flask, jsonify
from FlaskAPI.config import Config  
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

from FlaskAPI.users.routes import users
from FlaskAPI.main.routes import main
from FlaskAPI.bugs.routes import bugs

app.register_blueprint(users)
app.register_blueprint(main)
app.register_blueprint(bugs)



@app.route('/bugs')
def bugs():
    
    bugs = []

    return jsonify({'bugs': bugs})