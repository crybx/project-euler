# Problem 4 - Largest palindrome product
#
# A palindromic number reads the same both ways. The largest palindrome made from the
# product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

import math


def is_palindrome(n):
    n = str(n)
    result = True
    digit_count = len(n)
    halfway = math.ceil(digit_count / 2)

    for i in range(0, halfway):
        if n[i] != n[digit_count - 1 - i]:
            return False

    return result


answer = 0
palindrome_count = 0

for term1 in range(999, 99, -1):
    for term2 in range(term1, 99, -1):
        product = term1 * term2
        if is_palindrome(product):
            # print(str(term1) + " * " + str(term2) + " = " + str(product))
            palindrome_count += 1
            if product > answer:
                answer = product
                break

print("Palindromes found = " + str(palindrome_count))
print("Problem 4: " + str(answer))
