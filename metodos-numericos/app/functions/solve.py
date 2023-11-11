from app.classes.nonlinear_equation_response import NonLinearEquations
from app.classes.derivatives_response import DerivativesResponse
from app.classes.dif_numer import DiffNumberResponse
from app.functions.plot import create_plot
from app.functions.methods.bisection_method import bisection_method
from app.functions.methods.false_rule import false_rule_method
from app.functions.methods.newton_method import newton_method
from app.functions.methods.secant_method import secant_method
from app.functions.create_function import create_function
from app.functions.methods.derivatives import *
from app.utils.convert_to_latex import convert_to_latex
from app.functions.methods.dif_num import *


def solve_non_linear_equation(form):
    func_str = form.get("equation")
    func = create_function(func_str)
    a = float(form.get("a"))
    tol = float(form.get("tol"))
    if form.get("method") == "1" or form.get("method") == "2":
        b = float(form.get("b"))
    root = 0
    iter_count = 0
    if form.get("method") == "1":
        root, iter_count = bisection_method(func, a, b, tol)
        plot_data = create_plot(a, b, func, func_str, root)
        solution = NonLinearEquations(convert_to_latex(func_str), root, iter_count, plot_data)
    if form.get("method") == "2":
        root, iter_count = false_rule_method(func, a, b, tol)
        plot_data = create_plot(a, b, func, func_str, root)
        solution = NonLinearEquations(convert_to_latex(func_str), root, iter_count, plot_data)
    if form.get("method") == "3":
        root, iter_count = newton_method(func, a, tol)
        plot_data = create_plot(a, None, func, func_str, root)
        solution = NonLinearEquations(convert_to_latex(func_str), root, iter_count, plot_data)
    if form.get("method") == "4":
        root, iter_count = secant_method(func, a, tol)
        plot_data = create_plot(a, None, func, func_str, root)
        solution = NonLinearEquations(convert_to_latex(func_str), root, iter_count, plot_data)
    return solution

def solve_derivatives(form):
    func_str = form.get("equation")
    func = create_function(func_str)
    x = float(form.get("x"))
    tol = float(form.get("tol"))
    iter_count = 0
    root = 0
    if form.get("method") == "1":
        root, iter_count = two_points(func, x, tol)
        plot_data = create_plot(None, None, func, func_str, root)
        solution = DerivativesResponse(convert_to_latex(func_str), root, iter_count, plot_data)
    if form.get("method") == "2":
        root, iter_count = three_points_forward_difference(func, x, tol)
        plot_data = create_plot(None,None, func, func_str, root)
        solution = DerivativesResponse(convert_to_latex(func_str), root, iter_count, plot_data)
    if form.get("method") == "3":
        root, iter_count = three_points_backward_difference(func, x, tol)
        plot_data = create_plot(None,None, func, func_str, root)
        solution = DerivativesResponse(convert_to_latex(func_str), root, iter_count, plot_data)
    if form.get("method") == "4":
        root, iter_count = three_points_centered_difference(func, x, tol)
        plot_data = create_plot(None,None, func, func_str, root)
        solution = DerivativesResponse(convert_to_latex(func_str), root, iter_count, plot_data)
    return solution


def solve_dif_number(form):
    func_str = form.get("equation")
    func = create_function(func_str)
    a = float(form.get("a"))
    b = float(form.get("b"))
    n = int(form.get("n"))
    root = 0
    if form.get("method") == "1":
        root = trapecio_compuesto(func, a, b, n)
        print("ROOOT: --------------: ", root)
        print("SOLUTION: --------------- : ", trapecio_compuesto(func, a, b, n))
        plot_data = create_plot(None, None, func, func_str, root)
        solution = DiffNumberResponse(convert_to_latex(func_str), root, n, plot_data)
    if form.get("method") == "2":
        root = simpson_rule_compuesta(func, a, b, n)
        plot_data = create_plot(a, b, func, func_str, root)
        solution = DiffNumberResponse(convert_to_latex(func_str), root, n, plot_data)
    if form.get("method") == "3":
        root = simpson_38_rule_compuesta(func, a, b, n)
        plot_data = create_plot(a, b, func, func_str, root)
        solution = DiffNumberResponse(convert_to_latex(func_str), root, n, plot_data)
    return solution
