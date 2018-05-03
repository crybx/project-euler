# Problem 3 - Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

n = 600851475143
n_sqr = math.ceil(math.sqrt(n))
answer = 0

primes = [2, 3, 5, 7, 11, 13, 17]

# This brute force builds a list of all
# primes up to the square root of n.
for i in range(17, n_sqr + 1):
    for prime in primes:
        if i % prime == 0:
            break
    else:
        primes.append(i)

for prime in reversed(primes):
    if n % prime == 0:
        answer = prime
        break;

print("Problem 3: " + str(answer))

# This works for the number in problem 3, but it has a bug
# for general cases. If the largest_prime is higher than
# n_sqr, it will return the smaller_prime that = n / largest_prime.
# example n = 486847
# n_sqr = 698
# factors are 71 and 6857
# 6857 is the correct answer, but 71 is returned.
