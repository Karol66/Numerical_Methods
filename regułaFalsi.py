import math

def licz_pochodne(f, x, h=1e-6):
    """
    Funkcja oblicza numerycznie wartości pierwszej i drugiej pochodnej funkcji f(x) w punkcie x.

    Parametry:
    f: funkcja, której pochodne mają zostać obliczone
    x: punkt, w którym pochodne są obliczane
    h: wartość kroku różniczkowania (domyślnie 1e-6)

    Zwraca:
    df1: wartość pierwszej pochodnej funkcji f(x) w punkcie x
    df2: wartość drugiej pochodnej funkcji f(x) w punkcie x
    """
    fx = f(x)
    fxh = f(x + h)
    fx2h = f(x + 2 * h)
    df1 = (fxh - fx) / h
    df2 = (fx2h - 2 * fxh + fx) / (h ** 2)
    return df1, df2

# Definiujemy funkcję
def f(x):
    return x**2

# Obliczamy pochodne w punkcie x=
x = float(input("Podaj punkt, w którym chcesz obliczyć pochodne funkcji: "))
df1, df2 = licz_pochodne(f, x)

# Wyświetlamy wyniki
print(f"Wartość pierwszej pochodnej funkcji sin(x) w punkcie x=1 wynosi: {df1}")
print(f"Wartość drugiej pochodnej funkcji sin(x) w punkcie x=1 wynosi: {df2}")

def metoda_regula_falsi(f, a, b, epsilon=1e-6):
    """
    Metoda Reguły Falsi służy do znajdowania przybliżonego miejsca zerowego funkcji f(x) na przedziale [a, b].

    Parametry:
    f: funkcja, dla której szukamy miejsca zerowego
    a, b: końce przedziału, na którym poszukujemy miejsca zerowego
    epsilon: wartość błędu (domyślnie 1e-6)

    Zwraca:
    x2: przybliżone miejsce zerowe funkcji f(x) na przedziale [a, b]
    """

    # Sprawdzamy warunek konieczny istnienia miejsca zerowego
    if f(a) * f(b) > 0:
        raise ValueError("Funkcja nie spełnia warunków istnienia miejsca zerowego na przedziale [a, b].")

    # Inicjalizujemy zmienne
    fa = f(a)
    fb = f(b)
    x2 = a
    df2 = 0

    while abs(fb) > epsilon:

        # Obliczamy wartości pochodnych funkcji w punkcie x2
        df1, df2 = licz_pochodne(f, x2)

        # Obliczamy wartość nowego punktu
        x3 = b - fb * (b - a) / (fb - fa - df2 * (b - a))

        # Sprawdzamy warunek stopu
        if abs(x3 - x2) < epsilon:
            break

        # Przesuwamy punkty
        a = b
        fa = fb
        b = x3
        fb = f(b)
        x2 = x3

    return x2

def f(x):
    return x ** 3 - 3 * x + 1

# Ustawiamy wartości początkowe
a = -1
b = 1
epsilon = 1e-6

# Wywołujemy funkcję
x0 = metoda_regula_falsi(f, a, b, epsilon)

# Wyświetlamy wyniki
print(f"Przybliżone miejsce zerowe funkcji f(x) = x ** 3 - 3 * x + 1 na przedziale [{a}, {b}] wynosi: {x0}")