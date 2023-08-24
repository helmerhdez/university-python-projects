from flask import Blueprint, render_template

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/about')
def about():
    return render_template('about.html')
