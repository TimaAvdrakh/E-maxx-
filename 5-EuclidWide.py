def gdp(a,b):
    if a == 0:
        x = 0
        y = 1
        return b
    d = gdp(b%a,a )