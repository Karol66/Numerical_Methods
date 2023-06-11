import math

def f(x):
    return math.exp(x**2)

def integrate_simpson(a, b, n):
    h = (b - a) / n
    sum = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            sum += 2 * f(x)
        else:
            sum += 4 * f(x)

    return (h / 3) * sum

# Parametry
a = 0
b = 1
n = 100

# Wywołanie wzoru parabol
result = integrate_simpson(a, b, n)

print("Wynik całkowania:", result)