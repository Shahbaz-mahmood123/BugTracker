from flask import render_template, Blueprint, request, jsonify

bugs= Blueprint('bugs', __name__)

@bugs.route('/bugs', methods=['POST'])
def bugstest():
    return 'bugs', 201

@bugs.route('/bugs')
def bugsJSON():
    
    bugs = []

    return jsonify({'bugs': bugs})