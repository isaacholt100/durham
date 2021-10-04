m = 5
n = 3*m
m = 2*m + n
n = 5*n - m
print(m, n)

m = 2
x = 3.14
y = m*(x+2)
print(m, x, y)
print(type(m), type(x), type(y))

x = 0.0002
print(x)
t = x + 1e9
print(t)
t = t - 1e9
print(t)

m = 2
print(m==2)
print(m==3)
print(m*m == m + m)
print(2*m > m + 3)
print(m)

m = 3 * m + 7
p = (m == 2*n + 17)
w = y - 0.28
j = m / 13
u = m**2
r = m**-2
print(m, p, w, j, u, r)
print(type(m), type(p), type(w), type(j), type(u), type(r))

def q(x):
    val = 2 + 3*x + 4*x**2
    return val

print(q(5))

def dist2 ( x1 , y1 , x2 , y2 ):
    dx = x2 - x1
    dy = y2 - y1
    return ( dx **2 + dy **2)**0.5

print(dist2(1, 3, 4, -1))
print(dist2(2, 1, 7, 13))

def dist_point(x0, y0, a, b, c):
    m = -a/b
    inv = b/a
    intercept = -c/b
    x_intersect = (b/a * x0 - c/b - y0) / (b/a + a/b)
    y_intersect = -c/b - (a/b * x_intersect)
    return dist2(x0, y0, x_intersect, y_intersect)

print(dist_point(2, -2, 1, -1, 0))
    
def intersection_point(m0, c0, m1, c1):
    x = (c1 - c0)/(m0 - m1)
    y = m0 * x + c
    return x, y

def dist_to_circle(x0, y0, x1, y1, r):
    dist = dist2(x0, y0, x1, y1)
    return abs(dist - r)

from math import factorial

def nchoosek(n: int, k: int):
    assert n > 0 and k > 0 and k <= n
    fact_n = factorial(n)
    fact_k = factorial(k)
    return fact_n // (fact_k * factorial(n - k))

print(nchoosek(5, 3))

def catalan(m: int):
    return nchoosek(m << 1, m) // (m + 1)

assert catalan(6) == 132

def unfair_probability(h: int, n: int, p: float):
    assert p <= 1.0 and p >= 0.0
    combos = nchoosek(n, h)
    return combos * p ** h * (1-p) ** (n - h)
    