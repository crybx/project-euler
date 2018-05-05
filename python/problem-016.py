# Problem 16 - Power digit sum
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?

power = 2**1000
digits = str(power)
digits = list(map(int, digits))
digit_sum = sum(digits)

print("Problem 16: " + str(digit_sum))
