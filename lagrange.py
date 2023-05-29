# cmd -> py -m pip install scipy

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import lagrange

#      x|-1|0|1|2
# y=f(x)| 3|1|2|-6
# n=3
# L3(x)=lambda0y0+lambda1y1+lambda2y2+lambda3y3
# lambda0 = [(x-0)(x-1)(x-2)]/[(-1-0)(-1-1)(-1-2)]=...=[x(x-1)(x-2)]/(-6)
# lambda1 = [(x+1)(x-1)(x-2)]/[(0+1)(0-1)(0-2)]=...=[(x^2-1)(x-2)]/2
# lambda2 = [(x+1)(x-0)(x-2)]/[(0+1)(0-1)(0-2)]
# lambda3 = ...


# mamy 4 punktów w zakresie -1...2 i obliczamy dla nich f(x)
x1 = np.linspace(-1, 2, 4)
y1 = [3, 1, 2, -6]

# wyznaczamy współczynniki
F = lagrange(x1, y1)


print(f'{F}')

#Lub
# ...




# Aproksymacja średniokwadratowa
# i|xi|yi|xi^0|xi^1|xi^2|xi^3|xi^4|yixi^0|yixi^1|yixi^2|
# 0|-2| 0|   1|  -2|   4|  -8|  16|     0|     0|     0|
# 1| 1| 2|   1|   1|   1|   1|   1|     2|     2|     2|
# 2| 2| 3|   1|   2|   4|   8|  16|     3|     6|    12|
#         S0=3 S1=1 S2=9 S3=1 S4=33  t0=5   t1=8  t2=14
# n=2
# F2(x)=a2x^2+a1x+a0
#
#   S0a0+S1a1+S2a2=t0
# { S1a0+S2a1+S3a2=t1
#   S2a0+S3a1+S4a2=t2
#
# Wynik: a0 = 1/6 a1 = 3/4 a2 = 1/12




