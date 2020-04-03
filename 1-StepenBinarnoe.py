
def times(a,n):
    if n == 1:
        return a
    if n%2 != 0:
        return times(a, n-1) * a
    else:
        some = times(a, n/2)
        return some * some

print(times(2,4))