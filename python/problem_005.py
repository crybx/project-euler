# Problem 5 - Smallest multiple
#
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

n = 0
answer = 0

while answer == 0:
    n += 20

    for i in range(1, 21):
        if n % i != 0:
            break
    else:
        answer = n

print("Problem 5: " + str(answer))
