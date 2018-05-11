# Problem 23 - Non-abundant sums
#
# A perfect number is a number for which the sum of its proper
# divisors is exactly equal to the number. For example, the sum
# of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28,
# which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors
# is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16,
# the smallest number that can be written as the sum of two abundant
# numbers is 24. By mathematical analysis, it can be shown that all
# integers greater than 28123 can be written as the sum of two abundant
# numbers. However, this upper limit cannot be reduced any further by
# analysis even though it is known that the greatest number that cannot
# be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as
# the sum of two abundant numbers.

import math
import time


def divisor_sum(num):
    num_sqr = math.floor(math.sqrt(num))
    divisors = [1]

    for i in range(2, num_sqr + 1):
        if num % i == 0 and i * i != num:
            divisors.append(i)
            divisors.append(int(num / i))
        elif i * i == num:
            divisors.append(i)

    return sum(divisors)


def is_sum_of_abundants(abundants, num):
    for abundt in abundants:
        if abundt > num:
            return False

        diff = num - abundt
        if diff in abundants:
            return True

    return False


start_time = time.time()
abundant_nums = list()
limit = 28123

for n in range(1, limit):
    n_sum = divisor_sum(n)
    if n_sum > n:
        abundant_nums.append(n)

non_abundant_sums = list()

for n in range(1, 20162):
    if not is_sum_of_abundants(abundant_nums, n):
        # print("Non abundant added: " + str(n))
        non_abundant_sums.append(n)

answer = sum(non_abundant_sums)

print("Problem 23: " + str(answer))
print("{} ms".format(round(1000 * (time.time() - start_time))))

# 320802 ms
