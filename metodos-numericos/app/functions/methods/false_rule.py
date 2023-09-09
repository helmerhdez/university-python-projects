def false_rule_method(func, a, b, tol):
    if func(a) * func(b) >= 0:
        print("The function does not have a root in the interval")
        return None

    iter_count = 0
    while (b - a) / 2 > tol:
        c = a - func(a) * (b - a) / (func(b) - func(a))
        if func(c) == 0:
            break
        elif func(c) * func(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return c, iter_count
