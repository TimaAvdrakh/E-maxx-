



def fib(n):
    a = 0
    b = 1

    while n-1!= 0:
        a,b = b,a+b
        n -= 1
    return b

print(fib(4))