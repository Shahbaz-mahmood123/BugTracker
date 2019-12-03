from flask import render_template, Blueprint, request

users= Blueprint('users', __name__)

@users.route('/', methods=['POST'])
def hello():
    return 'Done', 201
