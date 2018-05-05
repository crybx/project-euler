# Problem 10 - Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import time

start_time = time.time()
n = 2000000
result = 0
primes = list()

# This builds a list of all primes less than n.
for i in range(2, n):
    for prime in primes:
        if i % prime == 0:
            break
    else:
        print(i)
        primes.append(i)

result = sum(primes)
print("Problem 10: " + str(result))
print("{} ms".format(round(1000 * (time.time() - start_time))))

# Okay, I really liked this method of collecting all the primes in a list until
# this problem (came up with in problem 3, and used in 7 too). This got the
# right answer, but took about 15 minutes to run. May need to revisit this.

# 2nd run: 918931 ms = 15.3 minutes on a laptop
