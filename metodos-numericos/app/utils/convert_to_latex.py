from sympy import symbols, latex, simplify
from sympy.parsing.sympy_parser import parse_expr

def convert_to_latex(function_str):
    x = symbols('x')

    try:
        expression = parse_expr(function_str)
        simplified_expression = simplify(expression)
        latex_representation = latex(simplified_expression)
        return f"$$f'(x) \\approx {latex_representation}$$"
    except Exception as e:
        return f"Error al procesar la función: {str(e)}"