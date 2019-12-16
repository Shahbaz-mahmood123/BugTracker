from flask import render_template, Blueprint, request

users= Blueprint('users', __name__)

@users.route('/users', methods=['POST'])
def hello():
    return 'Done', 201

@users.route('/', methods=['POST'])
def Home():
    return 'backend API', 201
