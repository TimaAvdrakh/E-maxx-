
def func(k,b,r):
    x1 = -b + 2*((b**2*(8*k -1) +(r**2)*((k-1)**2))**0.5)
    x2 = -b - 2 * ((b ** 2 * (8 * k - 1) + (r ** 2) * ((k - 1) ** 2)) ** 0.5)
    y1 = k*x1 + b
    y2 = k*x2 + b