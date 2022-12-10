import csv

import numpy as np

tree_map = np.zeros((99, 99))


def determine_scenic_score(_tree_map: np.array, start_row: int, start_col: int) -> int:
    tree_height = _tree_map[start_row][start_col]

    component_one_sum = 0
    component_two_sum = 0
    component_three_sum = 0
    component_four_sum = 0

    for _row in range(start_row + 1, 99, 1):
        component_one_sum += 1
        height = _tree_map[_row][start_col]
        if height >= tree_height:
            break

    for _row in range(start_row - 1, -1, -1):
        component_two_sum += 1
        if _tree_map[_row][start_col] >= tree_height:
            break

    for _col in range(start_col + 1, 99, 1):
        component_three_sum += 1
        if _tree_map[start_row][_col] >= tree_height:
            break

    for _col in range(start_col - 1, -1, -1):
        component_four_sum += 1
        if _tree_map[start_row][_col] >= tree_height:
            break

    return component_one_sum * component_two_sum * component_three_sum * component_four_sum


with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row_idx, row in enumerate(csv_reader):
        for col_idx, number in enumerate(row[0]):
            tree_map[row_idx, col_idx] = int(number)


max_scenic_score = 0
for row in range(1, 98, 1):
    for col in range(1, 98, 1):
        if determine_scenic_score(tree_map, row, col) > max_scenic_score:
            max_scenic_score = determine_scenic_score(tree_map, row, col)


print(f'Max scenic score = {max_scenic_score}')
