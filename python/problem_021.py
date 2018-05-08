# Problem 21 - Amicable numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).

# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import time
import math

def divisor_sum(num):
	total = 0
	num_sqr = math.ceil(math.sqrt(num))
	divisors = [1]
	
	for i in range(2, num_sqr + 1):
		if num % i == 0 and i * i != num:
			divisors.append(i)
			divisors.append(int(num / i))
		elif i * i == num:
			divisors.append(i)

	return sum(divisors)


start_time = time.time()

all_divisors_sums = dict()
amicable_divisor_sums = dict()
limit = 10000

for n in range(1, limit + 1):
	all_divisors_sums[n] = divisor_sum(n)
	
for n in range(1, limit + 1):
	this_sum = all_divisors_sums[n]
	
	if 1 < this_sum <= 10000 and n != this_sum:
		friend_sum = all_divisors_sums[this_sum]
		
		if n == friend_sum:
			amicable_divisor_sums[n] = this_sum
			amicable_divisor_sums[this_sum] = n
			
print(amicable_divisor_sums)
answer = sum(amicable_divisor_sums)

print("Problem 21: " + str(answer))
print("{} ms".format(round(1000 * (time.time() - start_time))))

