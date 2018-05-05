# Problem 12 - Highly divisible triangular number
#
# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first
# ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#
#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over five hundred divisors?

import time
import math

start_time = time.time()
i = 1
triangle = 1
answer = 0
highest_divisors = 2

while answer == 0:
    i += 1
    triangle += i
    divisors = 2
    tri_sqr = math.ceil(math.sqrt(triangle))

    for j in range(2, tri_sqr + 1):
        if triangle % j == 0 and j * j != triangle:
            divisors += 2
        elif j * j == triangle:
            divisors += 1

    if divisors > 500:
        answer = triangle

    if divisors > highest_divisors:
        highest_divisors = divisors
        print(str(triangle) + " - " + str(highest_divisors))


print("Problem 12: " + str(answer))
print("{} ms".format(round(1000 * (time.time() - start_time))))

# 8832 ms for correct answer
