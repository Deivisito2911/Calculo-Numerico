import math

def bisection_method(f, a, b, error):
    if f(a) * f(b) >= 0:
        return None
    else:
        iterations = 0
        while (b - a) / 2.0 > error:
            c = (a + b) / 2.0
            if f(c) == 0.0:
                return c, iterations
            elif f(c) * f(a) < 0:
                b = c
            else:
                a = c
            iterations += 1
        return (a + b) / 2.0, iterations

f = lambda x: (x - 2)**2 - math.log(x)
a = 1
b = 2
error = 0.04

root, iterations = bisection_method(f, a, b, error)

if root is not None:
    print(f"La raíz de la función es {root:.4f}.")
    print(f"El número de iteraciones que hizo el programa fue {iterations}.")
else:
    print("No se encontró ninguna raíz en el intervalo especificado.")
