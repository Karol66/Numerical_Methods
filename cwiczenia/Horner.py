def evaluate_polynomial(coefficients, x):
    result = 0
    for coefficient in coefficients:
        result = result * x + coefficient
    return result

# Współczynniki wielomianu
coefficients = [1, 0, 1, 2, 0, 0, -3]

# Punkt x
x = 5

# Obliczanie wartości wielomianu
result = evaluate_polynomial(coefficients, x)

print("Wartość wielomianu dla x=5:", result)