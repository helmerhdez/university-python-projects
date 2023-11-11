from math import *
def create_function(expression):
    try:
        def func(x):
            return eval(expression)

        return func
    except Exception as e:
        return None, str(e)