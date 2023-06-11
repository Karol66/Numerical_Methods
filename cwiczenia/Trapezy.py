import math

def f(x):
    return math.exp(x**2)

def integrate_trapezoidal(a, b, n):
    h = (b - a) / n
    sum = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        x = a + i * h
        sum += f(x)

    return h * sum

# Parametry
a = 0
b = 1
n = 100

# Wywołanie wzoru trapezów
result = integrate_trapezoidal(a, b, n)

print("Wynik całkowania:", result)