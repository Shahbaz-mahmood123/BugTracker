from flask import render_template, Blueprint, request
from FlaskAPI import mongo

main = Blueprint('main', __name__)

@main.route('/add', methods=['POST'])
def index():
    user_collection= mongo.db.users
    user_collection.insert({'name': 'Shahbaz'})
    return 'added user', 201