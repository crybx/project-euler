# This doesn't actually solve problem 3.
# I just wanted a program to test if a number is prime.

import math

def isPrime(n):
    n_sqr = math.ceil(math.sqrt(n))
    primes = list()

    # This brute force builds a list of all
    # primes up to the square root of n.
    for i in range(2, n_sqr + 1):
        for prime in primes:
            if i % prime == 0:
                break
        else:
            if n % i == 0:
                return False
            primes.append(i)

    return True


n = input('What integer do you want to check is prime?: ')
n = int(n)

if isPrime(n):
    print(str(n) + " is prime.")
else:
    print(str(n) + " is NOT prime.")
