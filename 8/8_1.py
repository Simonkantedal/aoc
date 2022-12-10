import csv

import numpy as np

tree_map = np.zeros((99, 99))
vis_map = np.zeros((99, 99))


with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row_idx, row in enumerate(csv_reader):
        for col_idx, number in enumerate(row[0]):
            tree_map[row_idx, col_idx] = int(number)


for row in range(1, 98, 1):
    current_height = tree_map[row][0]
    for col in range(1, 98, 1):
        if tree_map[row][col] > current_height:
            current_height = tree_map[row][col]
            vis_map[row][col] = 1.0


for col in range(1, 98, 1):
    current_height = tree_map[0][col]
    for row in range(1, 98, 1):
        if tree_map[row][col] > current_height:
            current_height = tree_map[row][col]
            vis_map[row][col] = 1.0


for row in range(1, 98, 1):
    current_height = tree_map[row][98]
    for col in range(97, 0, -1):
        if tree_map[row][col] > current_height:
            current_height = tree_map[row][col]
            vis_map[row][col] = 1.0


for col in range(97, 0, -1):
    current_height = tree_map[98][col]
    for row in range(97, 0, -1):
        if tree_map[row][col] > current_height:
            current_height = tree_map[row][col]
            vis_map[row][col] = 1.0


for row in range(99):
    vis_map[row][0] = 1
    vis_map[row][-1] = 1

for col in range(99):
    vis_map[0][col] = 1
    vis_map[-1][col] = 1


print(f'Sum of vis_map = {int(sum(sum(vis_map)))}')
