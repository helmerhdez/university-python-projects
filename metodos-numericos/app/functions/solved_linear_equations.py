from app.classes.nonlinear_equation_response import NonLinearEquations;
from app.functions.plot import create_plot;
from math import *
def solved_linear_equation(form):
    func_str = form.get('equation')
    func = create_function(func_str)
    a = float(form.get('a'))
    b = float(form.get('b'))
    tol = float(form.get('tol'))
    root = 0
    iter_count = 0
    if form.get('method') == '1':
        root, iter_count = bisection_method(func, a, b, tol)
    plot_data = create_plot(a, b, func, func_str)
    equation_solved = NonLinearEquations(func_str, root, iter_count, plot_data);
    return equation_solved

def bisection_method(func, a, b, tol):
    if func(a) * func(b) >= 0:
        return None

    iter_count = 0
    while (b - a) / 2 > tol:
        c = (a + b) / 2
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2, iter_count

def create_function(expression):
    def func(x):
        return eval(expression)
    return func
