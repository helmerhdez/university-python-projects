def newton_method(func, x, tol):
    iter_count = 0
    x = x

    while True:
        dfx = approximate_derivative(func, x)
        if dfx == 0:
            return None, iter_count

        x_new = x - func(x) / dfx
        iter_count += 1

        if abs(x_new - x) < tol:
            break

        x = x_new

    return x, iter_count

def approximate_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)