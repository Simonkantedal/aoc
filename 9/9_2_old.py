import csv
import math
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class Knot:
    x: int
    y: int


class Rope:
    def __init__(self):
        self.head = Knot(0, 0)
        self.tail = [
            Knot(0, 0), Knot(0, 0), Knot(0, 0), Knot(0, 0), Knot(0, 0), Knot(0, 0), Knot(0, 0), Knot(0, 0), Knot(0, 0)
        ]
        self.tail_positions = [(0, 0)]

    def move_head(self, _direction: str, _steps: int) -> None:
        for step in range(_steps):
            match _direction:
                case 'R':
                    self.head.x += 1
                case 'L':
                    self.head.x -= 1
                case 'U':
                    self.head.y += 1
                case 'D':
                    self.head.y -= 1
            move_vector = self._update_first_knot(_direction)
            for idx, current_knot in enumerate(self.tail[1:], start=1):
                previous_knot = self.tail[idx - 1]
                current_knot = self._update_subsequent_knot(current_knot, previous_knot, move_vector)
                self.tail[idx] = current_knot
                if (self.tail[-1].x, self.tail[-1].y) not in self.tail_positions:
                    self.tail_positions.append((self.tail[-1].x, self.tail[-1].y))

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

    def _update_first_knot(self, _direction) -> tuple[int, int]:
        distance = math.dist([self.head.x, self.head.y], [self.tail[0].x, self.tail[0].y])
        old_position = (self.tail[0].x, self.tail[0].y)
        new_position = old_position
        if distance > 1.5:
            match _direction:
                case 'R':
                    new_position = (self.head.x - 1, self.head.y)
                case 'L':
                    new_position = (self.head.x + 1, self.head.y)
                case 'U':
                    new_position = (self.head.x, self.head.y - 1)
                case 'D':
                    new_position = (self.head.x, self.head.y + 1)
            self.tail[0].x = new_position[0]
            self.tail[0].y = new_position[1]
        move_vector = (new_position[0] - old_position[0], new_position[1] - old_position[1])
        return move_vector

    def _update_subsequent_knot(self, current_knot: Knot, previous_knot: Knot, move_vector: tuple[int, int]):
        distance = math.dist([current_knot.x, current_knot.y], [previous_knot.x, previous_knot.y])
        if distance > 1.5:
            current_knot.x += move_vector[0]
            current_knot.y += move_vector[1]
        return current_knot


snake = Rope()


with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        direction, steps_str = row[0].split(' ')
        steps = int(steps_str)
        print(f'Head before move: {snake.head}')
        print(f'Tail before move: {snake.tail}')
        snake.move_head(direction, steps)
        print(f'Head after move: {snake.head}')
        print(f'Tail after move: {snake.tail}')
        print('=================================')

print(f'Number of tail positions: {len(snake.tail_positions)}')
