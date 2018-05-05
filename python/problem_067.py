# Problem 67 - Larger version of problem 18.
#
# Find the maximum total from top to bottom in
# triangle.txt (problem_067_original_triangle.txt in my repo),
# a 15K text file containing a triangle with one-hundred rows.

import problem_067_triangle as problem67
import problem_018_max_path_sum as problem18
import time

start_time = time.time()
triangle = problem67.get_triangle()
answer = problem18.max_path_sum(triangle)

print("Problem 67: " + str(answer))
print("{} ms".format(round(1000 * (time.time() - start_time))))

# 0 ms
