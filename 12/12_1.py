from __future__ import annotations

import csv
from dataclasses import dataclass

from string import ascii_lowercase

import numpy as np
import sys

sys.setrecursionlimit(25000)

LETTER_TO_INDEX = {letter: idx for idx, letter in enumerate(ascii_lowercase)}
LETTER_TO_INDEX["S"] = 0
LETTER_TO_INDEX["E"] = 0


height_map = np.zeros((41, 80))
distance_map = np.zeros((41, 80))


@dataclass
class Cell:
    height: int
    position: tuple[int, int]
    neighbor_positions: list[tuple]
    distance: int = 9999
    visited: bool = False


def get_cells(_height_map: np.array) -> dict[tuple, Cell]:
    neighbor_increments = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    _cells = {}
    for _row in range(41):
        for _col in range(80):
            neighbor_positions = [
                (_row + neighbor_increment[0], _col + neighbor_increment[1])
                for neighbor_increment in neighbor_increments
                if not _row + neighbor_increment[0] < 0
                and not _col + neighbor_increment[1] < 0
                and not _row + neighbor_increment[0] > 40
                and not _col + neighbor_increment[1] > 79
                and _height_map[
                    _row + neighbor_increment[0], _col + neighbor_increment[1]
                ]
                - _height_map[_row, _col]
                < 2
            ]
            cell = Cell(
                height=_height_map[_row, _col],
                position=(_row, _col),
                neighbor_positions=neighbor_positions,
            )
            _cells[(_row, _col)] = cell
    return _cells


def populate_distance_map(_cells, _cell: Cell, _distance_map):
    for neighbor_position in _cell.neighbor_positions:
        neighbor_cell = _cells[neighbor_position]
        old_distance = neighbor_cell.distance
        new_distance = _cell.distance + 1
        if new_distance < old_distance:
            neighbor_cell.distance = new_distance
            _distance_map[neighbor_cell.position[0], neighbor_cell.position[1]] = new_distance
            populate_distance_map(_cells, neighbor_cell, _distance_map)
        # if not neighbor_cell.visited:
        #     neighbor_cell.visited = True
        #     populate_distance_map(_cells, neighbor_cell, _distance_map)
        # else:
        #     print('visited')


def get_distance(_cells, cell: Cell, _distance: int) -> int:
    for neighbor_position in cell.neighbor_positions:
        neighbor_cell = _cells[neighbor_position]
        _distance += 1
        if neighbor_cell.position == (20, 55):
            print(f"Distance = {_distance}")
            get_distance(_cells, neighbor_cell, _distance)
        else:
            get_distance(_cells, neighbor_cell, _distance)


with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row_idx, row in enumerate(csv_reader):
        for col_idx, letter in enumerate(row[0]):
            height_map[row_idx, col_idx] = LETTER_TO_INDEX[letter]


start_cell = Cell(
    height=0,
    position=(20, 0),
    neighbor_positions=[(19, 0), (20, 1), (21, 0)],
    distance=0,
    visited=True,
)


cells = get_cells(height_map)
cells[(20, 0)] = start_cell
for distance_map_row in range(41):
    for distance_map_col in range(80):
        distance_map[distance_map_row, distance_map_col] = 999
distance_map[20, 0] = 0
populate_distance_map(cells, start_cell, distance_map)
