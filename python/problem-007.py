# Problem 7 - 10001st prime
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

n = 10001
i = 2
primes = list()

# Builds a list of the first n primes.
while len(primes) < n:

    for prime in primes:
        if i % prime == 0:
            break
    else:
        primes.append(i)
        # print(str(i) + " is prime #" + str(len(primes)))

    i += 1

print("Problem 7: " + str(primes[n - 1]))
