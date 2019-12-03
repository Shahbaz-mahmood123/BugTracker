from flask import Flask 
from FlaskAPI.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def hello():
    return 'Hello, World!'

    return app