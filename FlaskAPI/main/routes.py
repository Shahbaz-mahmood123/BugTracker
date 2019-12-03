from flask import render_template, Blueprint, request

main = Blueprint('main', __name__)

@main.route('/main', methods=['POST'])
def post():
    return 'main routes', 201
