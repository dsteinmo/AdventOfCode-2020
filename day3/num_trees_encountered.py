#!/usr/bin/python3

def count_trees_encountered(rows: [str], stride_right = 3, stride_down = 1) -> int:
    num_cols = len(rows[0])
    num_rows = len(rows)

    curr_row = 0
    curr_col = 0

    num_trees = 0

    while (curr_row < num_rows):
        if rows[curr_row][curr_col] == "#":
            num_trees += 1

        curr_col = (curr_col + stride_right)  # shift right.
        curr_col %= (num_cols - 1)  # deal with right-ward periodicity.

        curr_row += stride_down

    return num_trees

rows = []
#with open("day3_input_sample.txt", mode="r") as f:
with open("day3_input.txt", mode="r") as f:
    rows = f.readlines()


print("Day 3")
print("=====")

num_trees = count_trees_encountered(rows, 3, 1)

print(f"Part 1: Number of trees encountered: {num_trees}")
    
# part 2:
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
product = 1
for slope in slopes:
    num_trees = count_trees_encountered(rows, stride_right=slope[0], stride_down=slope[1])
    print(num_trees)
    product *= num_trees

print(f"Part 2: Product of all tree counts: {product}")