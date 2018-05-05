# Problem 51 - Prime digit replacements
#
# By replacing the 1st digit of the 2-digit number *3, it turns out that six
# of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this
# 5-digit number is the first example having seven primes among the ten
# generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
# 56773, and 56993. Consequently 56003, being the first member of this family,
# is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an eight prime
# value family.

import math
import time


def is_prime(n):
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


def has_repeats(n):
    if len(str(n)) > 10:
        return True
    return len(set([c for c in str(n)])) != len(str(n))


def number_of_digit_in_n(digit, n):
    count = 0
    while n > 0:
        if n % 10 == digit:
            count = count + 1

        n = n // 10

    return count


def replace_digit_in_n(digit, replace, n):
    digit = str(digit)
    replace = str(replace)
    n = str(n)
    shiny_new_number = n.replace(digit, replace)
    return int(shiny_new_number)


start_time = time.time()
primes = list()
result = 0
i = 1

# This builds a list of all primes less than n.
while result == 0:
    i += 1

    for prime in primes:
        if i % prime == 0:
            break
    else:
        primes.append(i)
        if has_repeats(i):
            for digit in range(0, 10):
                if number_of_digit_in_n(digit, i) > 1:
                    family_count = 0
                    size = len(str(i))

                    for replacement in range(0, 10):
                        num = replace_digit_in_n(digit, replacement, i)

                        # Making sure the size of the new number is the same prevents
                        # something starting with 0 from counting like 111857 -> 000857
                        if len(str(num)) == size and is_prime(num):
                            family_count += 1

                    # if family_count >= 7:
                    #    print("Prime = " + str(i) + ", family count = " + str(family_count))

                    if family_count >= 8:
                        result = i

print(result)
print("{} ms".format(round(1000 * (time.time() - start_time))))

# 7515 ms - Brute force, first working idea, no attempt to optimize.
