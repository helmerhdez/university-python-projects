def two_points(func, x, h=0.1, tol=1e-6):
    previous_derivative = None
    current_derivative = (func(x + h) - func(x)) / h
    iter_count = 1

    while previous_derivative is None or abs(current_derivative - previous_derivative) > tol:
        h /= 10
        previous_derivative = current_derivative
        current_derivative = (func(x + h) - func(x)) / h
        iter_count += 1

    return current_derivative, iter_count

def three_points_forward_difference(func, x, h=0.1, tol=1e-6):
    previous_derivative = None
    current_derivative = (-3 * func(x) + 4 * func(x + h) - func(x + 2 * h)) / (2 * h)
    iter_count = 1

    while previous_derivative is None or abs(current_derivative - previous_derivative) > tol:
        h /= 10
        previous_derivative = current_derivative
        current_derivative = (-3 * func(x) + 4 * func(x + h) - func(x + 2 * h)) / (2 * h)
        iter_count += 1

    return current_derivative, iter_count

def three_points_backward_difference(func, x, h=0.1, tol=1e-6):
    previous_derivative = None
    current_derivative = (func(x - 2 * h) - 4 * func(x - h) + 3 * func(x)) / (2 * h)
    iter_count = 1

    while previous_derivative is None or abs(current_derivative - previous_derivative) > tol:
        h /= 10
        previous_derivative = current_derivative
        current_derivative = (func(x - 2 * h) - 4 * func(x - h) + 3 * func(x)) / (2 * h)
        iter_count += 1

    return current_derivative, iter_count

def three_points_centered_difference(func, x, h=0.1, tol=1e-6):
    previous_derivative = None
    current_derivative = (func(x + h) - func(x - h)) / (2 * h)
    iter_count = 1

    while previous_derivative is None or abs(current_derivative - previous_derivative) > tol:
        h /= 10
        previous_derivative = current_derivative
        current_derivative = (func(x + h) - func(x - h)) / (2 * h)
        iter_count += 1

    return current_derivative, iter_count