def secant_method(func, x0, tol, delta=1e-4):
    iter_count = 0
    x1 = x0 + delta

    while True:
        y0, y1 = func(x0), func(x1)
        if y1 - y0 == 0:
            return None, iter_count

        x_new = x1 - y1 * (x1 - x0) / (y1 - y0)

        iter_count += 1
        if abs(x_new - x1) < tol:
            return x_new, iter_count

        x0, x1 = x1, x_new