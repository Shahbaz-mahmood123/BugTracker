import os

class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')
        MONGO_URI =  'mongodb+srv://Shahbaz:Kickboxing123%21%21@flaskapi-3y5v5.mongodb.net/test?retryWrites=true&w=majority'
        #SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')