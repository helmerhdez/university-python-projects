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
