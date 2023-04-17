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


def metoda_siecznych(f, x0, x1, epsilon=1e-6, max_iter=100):
    """
    Funkcja oblicza przybliżone miejsce zerowe funkcji f(x) oraz wartość pochodnej w tym punkcie
    za pomocą metody siecznych.

    Parametry:
    f: funkcja, której miejsce zerowe ma zostać znalezione
    x0: pierwsza wartość początkowa zmiennej x
    x1: druga wartość początkowa zmiennej x
    epsilon: dokładność obliczeń (domyślnie 1e-6)
    max_iter: maksymalna liczba iteracji (domyślnie 100)

    Zwraca:
    x2: przybliżone miejsce zerowe funkcji f(x)
    df: wartość pochodnej funkcji f(x) w punkcie x2
    """
    # Obliczenie pochodnych funkcji w punktach x0 i x1
    df0, df1 = licz_pochodne(f, x0)[0], licz_pochodne(f, x1)[0]

    # Iteracyjne wyznaczanie kolejnych przybliżeń miejsca zerowego
    i = 0
    while abs(f(x1)) > epsilon and i < max_iter:
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        df2 = licz_pochodne(f, x2)[0]
        x0, x1 = x1, x2
        df0, df1 = df1, df2
        i += 1

    # Sprawdzenie, czy osiągnięto maksymalną liczbę iteracji
    if i == max_iter:
        print("Nie osiągnięto wymaganej dokładności w maksymalnej liczbie iteracji")

    return x2, df2

def h(x):
    return x**3 + x - 1

x0 = float(input("Podaj pierwszy punkt startowy: "))
x1 = float(input("Podaj drugi punkt startowy: "))
x2, df2 = metoda_siecznych(h, x0, x1)

print(f"Przybliżone miejsce zerowe funkcji h(x) = x**3 + x - 1 wynosi: {x2}")
print(f"Wartość pochodnej funkcji h(x) w punkcie x2 wynosi: {df2}")