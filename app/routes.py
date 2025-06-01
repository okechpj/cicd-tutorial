from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to the Advanced Flask App and CI/CD pipeline!"
