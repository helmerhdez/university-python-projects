def create_function(expression):
    def func(x):
        return eval(expression)

    return func
