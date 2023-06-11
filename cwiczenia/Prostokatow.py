import math

def f(x):
    return math.exp(x**2)

def integrate_rectangular(a, b, n):
    h = (b - a) / n
    sum = 0

    for i in range(n):
        x = a + i * h
        sum += f(x)

    return h * sum

# Parametry
a = 0
b = 1
n = 100

# Wywołanie metody prostokątów
result = integrate_rectangular(a, b, n)

print("Wynik całkowania:", result)