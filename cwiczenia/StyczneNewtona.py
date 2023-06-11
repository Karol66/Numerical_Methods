def f(x):
    return x**3 + x - 1

def f_derivative(x):
    return 3*x**2 + 1

def newton_raphson_method(x, epsilon):
    while True:
        x_new = x - f(x) / f_derivative(x)
        if abs(x_new - x) < epsilon:
            break
        x = x_new
    return x_new

# Parametry
x_initial = 0.5
epsilon = 0.00001

# Wywołanie metody stycznych Newtona
root = newton_raphson_method(x_initial, epsilon)

print("Pierwiastek równania: ", root)