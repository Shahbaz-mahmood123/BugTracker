from flask import render_template, Blueprint, request

bugs= Blueprint('bugs', __name__)

@bugs.route('/bugs', methods=['POST'])
def bugstest():
    return 'bugs', 201
