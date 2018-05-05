# Problem 14 - Longest Collatz sequence
#
# The following iterative sequence is defined for the set of positive integers:
#
# n -> n/2 (n is even)
# n -> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#
# It can be seen that this sequence (starting at 13 and finishing at 1)
# contains 10 terms. Although it has not been proved yet (Collatz Problem),
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.

import time

start_time = time.time()
longest_chain = 0
answer = 0

for i in range(2, 1000000):
    current_val = i
    current_chain = 0

    while current_val != 1:
        current_chain += 1

        # Rules given for calculating next item in chain.
        if current_val % 2 == 0:
            current_val = current_val // 2
        else:
            current_val = current_val * 3 + 1

    if current_chain > longest_chain:
        longest_chain = current_chain
        answer = i

print("Longest chain: " + str(longest_chain))
print("Problem 14: " + str(answer))
print("{} ms".format(round(1000 * (time.time() - start_time))))

# 23666 ms
