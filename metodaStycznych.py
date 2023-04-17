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


def metoda_stycznych(f, x0, epsilon=1e-6, max_iter=100):
    """
    Funkcja oblicza przybliżone miejsce zerowe funkcji f(x) oraz wartość pochodnej w tym punkcie
    za pomocą metody stycznych.

    Parametry:
    f: funkcja, której miejsce zerowe ma zostać znalezione
    x0: wartość początkowa zmiennej x
    epsilon: dokładność obliczeń (domyślnie 1e-6)
    max_iter: maksymalna liczba iteracji (domyślnie 100)

    Zwraca:
    x1: przybliżone miejsce zerowe funkcji f(x)
    df: wartość pochodnej funkcji f(x) w punkcie x1
    """
    # Obliczenie pochodnej funkcji w punkcie x0
    df = licz_pochodne(f, x0)[0]

    # Sprawdzenie, czy pochodna w punkcie x0 jest równa 0
    if abs(df) < epsilon:
        raise ValueError("Pochodna w punkcie x0 wynosi 0")

    # Iteracyjne wyznaczanie kolejnych przybliżeń miejsca zerowego
    x1 = x0 - f(x0) / df
    i = 1
    while abs(f(x1)) > epsilon and i < max_iter:
        df = licz_pochodne(f, x1)[0]
        if abs(df) < epsilon:
            raise ValueError("Pochodna w punkcie x1 wynosi 0")
        x1 = x1 - f(x1) / df
        i += 1

    # Sprawdzenie, czy osiągnięto maksymalną liczbę iteracji
    if i == max_iter:
        print("Nie osiągnięto wymaganej dokładności w maksymalnej liczbie iteracji")

    return x1, df

def g(x):
    return x**2 - 4

x0 = float(input("Podaj punkt startowy: "))
x1, df = metoda_stycznych(g, x0)

print(f"Przybliżone miejsce zerowe funkcji g(x) = x**2 - 4 wynosi: {x1}")
print(f"Wartość pochodnej funkcji g(x) = x**2 - 4 w punkcie x={x1} wynosi: {df}")