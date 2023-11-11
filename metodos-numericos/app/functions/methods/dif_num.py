def simpson_rule_compuesta(func, a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser un número par para la regla de Simpson 1/3")

    h = (b - a) / n
    suma = func(a) + func(b)

    for i in range(1, n):
        factor = 4 if i % 2 != 0 else 2
        suma += factor * func(a + i * h)

    return (h / 3) * suma


def simpson_38_rule_compuesta(func, a, b, n):
    if n % 3 != 0:
        raise ValueError("n debe ser divisible por 3 para la regla de Simpson 3/8")

    h = (b - a) / n
    suma = func(a) + func(b)

    for i in range(1, n):
        if i % 3 == 0:
            factor = 2
        else:
            factor = 3
        suma += factor * func(a + i * h)

    return (3 * h / 8) * suma

def trapecio_compuesto(func, a, b, n):
    h = (b - a) / n
    suma = 0.5 * (func(a) + func(b))

    for i in range(1, n):
        suma += func(a + i * h)
        
    print("SUMA: -------: ", h * suma)
    return h * suma