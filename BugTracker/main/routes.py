from flask import render_template, Blueprint, request
from BugTracker import mongo

main = Blueprint('main', __name__)

@main.route('/home')
def home():
    return render_template('home.html')