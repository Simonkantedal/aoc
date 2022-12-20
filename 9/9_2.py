import csv
import math
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Knot:
    x: int
    y: int
    idx: int


class Rope:
    def __init__(self):
        self.knots = [
            Knot(0, 0, 0), Knot(0, 0, 1), Knot(0, 0, 2), Knot(0, 0, 3), Knot(0, 0, 4), Knot(0, 0, 5), Knot(0, 0, 6), Knot(0, 0, 7), Knot(0, 0, 8), Knot(0, 0, 9)
        ]
        self.tail_positions = [(0, 0)]

    def move_head(self, _direction: str, _steps: int) -> None:
        for step in range(_steps):
            match _direction:
                case 'R':
                    self._move_right(self.knots[0])
                case 'L':
                    self._move_left(self.knots[0])
                case 'U':
                    self._move_up(self.knots[0])
                case 'D':
                    self._move_down(self.knots[0])
            self._update_tail_positions()
            if (self.knots[9].x, self.knots[9].y) not in self.tail_positions:
                self.tail_positions.append((self.knots[9].x, self.knots[9].y))

    def _update_tail_positions(self):
        for idx, current_knot in enumerate(self.knots[1:]):
            previous_knot = self.knots[idx]
            distance_between_knots = self._compute_knot_distance(previous_knot, current_knot)
            if distance_between_knots > 1.5:
                self._move_knot_to_follow(previous_knot, current_knot)

    def _move_knot_to_follow(self, first_knot: Knot, second_knot: Knot):
        difference = (first_knot.x - second_knot.x, first_knot.y - second_knot.y)
        if difference[0] > 0 and difference[1] == 0:
            self._move_right(second_knot)
        elif difference[0] < 0 and difference[1] == 0:
            self._move_left(second_knot)
        elif difference[0] == 0 and difference[1] > 0:
            self._move_up(second_knot)
        elif difference[0] == 0 and difference[1] < 0:
            self._move_down(second_knot)
        elif difference[0] > 0 and difference[1] > 0:
            self._move_right_up(second_knot)
        elif difference[0] > 0 and difference[1] < 0:
            self._move_right_down(second_knot)
        elif difference[0] < 0 and difference[1] > 0:
            self._move_left_up(second_knot)
        elif difference[0] < 0 and difference[1] < 0:
            self._move_left_down(second_knot)

    def _compute_knot_distance(self, knot_a: Knot, knot_b: Knot) -> float:
        return math.dist([knot_a.x, knot_a.y], [knot_b.x, knot_b.y])

    def _move_right(self, knot: Knot) -> None:
        knot.x += 1

    def _move_left(self, knot: Knot) -> None:
        knot.x -= 1

    def _move_up(self, knot: Knot) -> None:
        knot.y += 1

    def _move_down(self, knot: Knot) -> None:
        knot.y -= 1

    def _move_right_up(self, knot: Knot) -> None:
        knot.x += 1
        knot.y += 1

    def _move_left_up(self, knot: Knot) -> None:
        knot.x -= 1
        knot.y += 1

    def _move_right_down(self, knot: Knot) -> None:
        knot.x += 1
        knot.y -= 1

    def _move_left_down(self, knot: Knot) -> None:
        knot.x -= 1
        knot.y -= 1


rope = Rope()

with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        direction, steps_str = row[0].split(' ')
        steps = int(steps_str)
        rope.move_head(direction, steps)
        # print(rope.knots)

print(f'Number of tail positions: {len(rope.tail_positions)}')
