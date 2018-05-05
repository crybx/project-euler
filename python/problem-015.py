# Problem 15
#
# Starting in the top left corner of a 2 by 2 grid, and only being able to move
# to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20 by 20 grid?

import math

# This question basically amounts to how many ways can you combine
# 20 downs and 20 rights. There is a combination formula.
# http://www.mathwords.com/c/combination_formula.htm
# C(40, 20) = 40! / (20! * 20!)

answer = math.factorial(40) / (math.factorial(20)**2)

print("Problem 15: " + str(answer))
