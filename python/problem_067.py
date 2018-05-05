# Problem 67 -

import problem_067_triangle as problem67
import problem_018_max_path_sum as problem18

triangle = problem67.get_triangle()
answer = problem18.max_path_sum(triangle)

print("Problem 67: " + str(answer))
