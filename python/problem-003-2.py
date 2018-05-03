# Problem 3 - Largest prime factor
#
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

n = 600851475143
factor = 2

while n / factor != 1:
    if n % factor == 0:
        # Uncomment to see more factors.
        #print(factor)
        n = n / factor

    factor += 1

print("Problem 3: " + str(factor))

# This solution works FOR THIS PROBLEM, but not in all general cases.
