numbers = list(range(1, 16))
primes, not_primes = [], []
a = 0
for i in range(2, 16):
    for j in range(2, i):
        if i % j == 0:
            a = 1
    if a == 0:
        primes.append(i)
    else:
        not_primes.append(i)
    a = 0
print(f"Primes: {primes}")
print(f"Not Primes: {not_primes}")
