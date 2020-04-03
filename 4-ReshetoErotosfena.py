def eratosthenes (n):
    primes = []
    multiples = []
    for i in range(2, n + 1):
        if i not in multiples:
            primes.append(i)
            multiples.extend(range(i * i, n + 1, i))
    return primes

print(eratosthenes(12))