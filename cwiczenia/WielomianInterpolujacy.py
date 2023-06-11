import numpy as np

# Podane punkty
x = np.array([0, 2, 3, 4, 5])
y = np.array([1, 3, 2, 5, 7])

# Wyznaczanie współczynników wielomianu interpolacyjnego
coefficients = np.polyfit(x, y, len(x)-1)

# Tworzenie wielomianu
polynomial = np.poly1d(coefficients)

# Obliczanie wartości wielomianu dla x=1
result = polynomial(1)

print("Wielomian interpolujący:")
print(polynomial)
print("Wartość wielomianu dla x=1:")
print(result)

x = [0, 2, 3, 4, 5]
y = [1, 3, 2, 5, 7]

# Funkcja do wyznaczania współczynników wielomianu interpolacyjnego
# def calculate_coefficients(x, y):
#     n = len(x)
#     coefficients = []

#     for i in range(n):
#         numerator = 1
#         denominator = 1
#         for j in range(n):
#             if j != i:
#                 numerator *= (x[i] - x[j])
#                 denominator *= (x[i] - x[j])
#         coefficients.append(sum(y[j] * numerator / denominator for j in range(n)))

#     return coefficients

# # Wyznaczanie współczynników wielomianu interpolacyjnego
# coefficients = calculate_coefficients(x, y)

# # Tworzenie wielomianu
# def polynomial_value(coefficients, x):
#     n = len(coefficients)
#     result = 0
#     for i in range(n):
#         term = coefficients[i]
#         for j in range(i):
#             term *= (x - x[j])
#         result += term
#     return result

# # Obliczanie wartości wielomianu dla x=1
# result = polynomial_value(coefficients, 1)

# print("Wielomian interpolujący:")
# print(coefficients)
# print("Wartość wielomianu dla x=1:")
# print(result)