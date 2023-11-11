from flask import Blueprint, render_template, redirect, url_for
from flask import request
from app.functions.solve import solve_non_linear_equation, solve_derivatives, solve_dif_number

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def index():
    return redirect(url_for('main_routes.home'))

@main_routes.route('/home')
def home():
    return render_template('home.html')

@main_routes.route('/nonlinear_equation')
def nonlinear_equation():
    return render_template('nonlinear_equation.html')

@main_routes.route('/about')
def about():
    return render_template('about.html')

@main_routes.route('/nonlinear_equation', methods=['POST'])
def nonlinear_equations():
    result = solve_non_linear_equation(request.form)
    return render_template('nonlinear_equation.html', result=result)

@main_routes.route('/derivatives')
def derivatives():
    return render_template('derivatives.html')

@main_routes.route('/derivatives-two-points', methods=['POST'])
def derivatives_two_points():
    result = solve_derivatives(request.form)
    return render_template('derivatives.html', result=result)

@main_routes.route('/dif_number')
def dif_number():
    return render_template('dif_number.html')

@main_routes.route('/dif_number', methods=['POST'])
def dif_numbers():
    result = solve_dif_number(request.form)
    return render_template('dif_number.html', result=result)

