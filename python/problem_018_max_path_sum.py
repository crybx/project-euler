def max_path_sum(triangle):

    levels = len(triangle)
    second_to_last = levels - 2

    for row in range(second_to_last, -1, -1):

        for col in range(0, len(triangle[row])):
            left = triangle[row + 1][col]
            right = triangle[row + 1][col + 1]
            triangle[row][col] += left if left > right else right

    return triangle[0][0]
