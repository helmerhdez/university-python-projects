from flask import Blueprint, render_template, redirect, url_for
from flask import request
from app.functions.solved_linear_equations import solved_linear_equation

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return redirect(url_for('main_routes.nonlinear_equation'))

@main_routes.route('/nonlinear_equation')
def nonlinear_equation():
    return render_template('nonlinear_equation.html')

@main_routes.route('/about')
def about():
    return render_template('about.html')

@main_routes.route('/nonlinear_equation', methods=['POST'])
def nonlinear_equations():
    result = solved_linear_equation(request.form)
    return render_template('nonlinear_equation.html', result=result)

