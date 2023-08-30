from app.classes.nonlinear_equation_response import NonLinearEquations
from app.functions.plot import create_plot
from app.functions.methods.bisection_method import bisection_method
from app.functions.methods.false_rule import false_rule_method
from app.functions.create_function import create_function
from math import *


def solve_equation(form):
    func_str = form.get("equation")
    func = create_function(func_str)
    a = float(form.get("a"))
    b = float(form.get("b"))
    tol = float(form.get("tol"))
    root = 0
    iter_count = 0
    plot_data = create_plot(a, b, func, func_str)
    if form.get("method") == "1":
        root, iter_count = bisection_method(func, a, b, tol)
        solution = NonLinearEquations(func_str, root, iter_count, plot_data)
    if form.get("method") == "2":
        root, iter_count = false_rule_method(func, a, b, tol)
        solution = NonLinearEquations(func_str, root, iter_count, plot_data)
    return solution
