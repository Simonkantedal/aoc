import csv
import math
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np


@dataclass
class SnakePart:
    x: int
    y: int


class Snake:
    def __init__(self):
        self.head = SnakePart(0, 0)
        self.tail = SnakePart(0, 0)
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
            self._update_tail_position(_direction)

    def _update_tail_position(self, _direction: str):
        distance = math.dist([self.head.x, self.head.y], [self.tail.x, self.tail.y])
        if distance > 1.5:
            match _direction:
                case 'R':
                    self.tail.x = self.head.x - 1
                    self.tail.y = self.head.y
                case 'L':
                    self.tail.x = self.head.x + 1
                    self.tail.y = self.head.y
                case 'U':
                    self.tail.y = self.head.y - 1
                    self.tail.x = self.head.x
                case 'D':
                    self.tail.y = self.head.y + 1
                    self.tail.x = self.head.x
        if (self.tail.x, self.tail.y) not in self.tail_positions:
            self.tail_positions.append((self.tail.x, self.tail.y))

    def visualise(self):
        width = max(
            math.dist([self.head.x, self.head.y], [self.tail.x, self.tail.y]),
            math.dist([self.head.x, self.head.y], [self.tail.x, self.tail.y])
        )
        canvas = np.zeros((int(np.ceil(width)), int(np.ceil(width))))
        canvas[snake.head.x, snake.head.y] = 1
        canvas[snake.tail.x, snake.tail.y] = 2
        print('debug')
        # plt.figure()
        # plt.imshow(canvas)
        # plt.show()


snake = Snake()


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
