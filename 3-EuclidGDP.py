def gdp(a,b):
    if b==0:
        return a
    else:
        return gdp(b,a%b)

print(gdp(12,5))