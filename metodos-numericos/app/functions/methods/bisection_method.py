def bisection_method(func, a, b, tol):
    try:
        if func(a) * func(b) >= 0:
            raise ValueError("La función no cambia de signo en el intervalo dado.")

        iterations = 0
        while abs(b - a) > tol:
            c = (a + b) / 2
            if func(c) == 0:
                return c, iterations
            elif func(c) * func(a) < 0:
                b = c
            else:
                a = c
            iterations += 1

        return (a + b) / 2, iterations
    except Exception as e:
        return None, str(e)