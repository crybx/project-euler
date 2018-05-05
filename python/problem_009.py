# Problem 9 - Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# Trying Euclid's formula: https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

n = 1
m = 2
result = 0

for i in range(2, 999):
    for j in range(1, 999):
        if j >= i:
            break

        m = i
        n = j

        a = m**2 - n**2
        b = 2 * m * n
        c = m**2 + n**2

        if a + b + c == 1000:
            result = a * b * c
            print(str(a) + "^2 + " + str(b) + "^2 = " + str(c) + "^2")
            print(str(a) + " + " + str(b) + " + " + str(c) + " = 1000")
            print(str(a) + " * " + str(b) + " * " + str(c) + " = " + str(result))

    if result > 0:
        break
