from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass
class Item:
    worry_level: int


class Monkey:
    def __init__(self, items: list[Item], operation_function, test_function):
        self.items = items
        self._operation_function = operation_function
        self._test_function = test_function
        self.num_inspections = 0
        self._lowest_common_denominator = 9699690

    def inspect(self, _item: Item) -> None:
        _item.worry_level = self._operation_function(_item.worry_level)
        mod = _item.worry_level % self._lowest_common_denominator
        _item.worry_level = mod
        self.num_inspections += 1

    def test_item(self, _item) -> int:
        return self._test_function(_item.worry_level)

    def throw_item(self, _item: Item, receiving_monkey: Monkey) -> None:
        receiving_monkey.items.append(_item)

    def remove_all_items(self):
        self.items = []


monkey_0 = Monkey(
    items=[Item(54), Item(61), Item(97), Item(63), Item(74)],
    operation_function=lambda x: x * 7,
    test_function=lambda x: 5 if x % 17 == 0 else 3,
)

monkey_1 = Monkey(
    items=[Item(61), Item(70), Item(97), Item(64), Item(99), Item(83), Item(52), Item(87)],
    operation_function=lambda x: x + 8,
    test_function=lambda x: 7 if x % 2 == 0 else 6,
)

monkey_2 = Monkey(
    items=[Item(60), Item(67), Item(80), Item(65)],
    operation_function=lambda x: x * 13,
    test_function=lambda x: 1 if x % 5 == 0 else 6,
)
monkey_3 = Monkey(
    items=[Item(61), Item(70), Item(76), Item(69), Item(82), Item(56)],
    operation_function=lambda x: x + 7,
    test_function=lambda x: 5 if x % 3 == 0 else 2,
)

monkey_4 = Monkey(
    items=[Item(79), Item(98)],
    operation_function=lambda x: x + 2,
    test_function=lambda x: 0 if x % 7 == 0 else 3,
)

monkey_5 = Monkey(
    items=[Item(72), Item(79), Item(55)],
    operation_function=lambda x: x + 1,
    test_function=lambda x: 2 if x % 13 == 0 else 1,
)

monkey_6 = Monkey(
    items=[Item(63)],
    operation_function=lambda x: x + 4,
    test_function=lambda x: 7 if x % 19 == 0 else 4,
)

monkey_7 = Monkey(
    items=[Item(72), Item(51), Item(93), Item(63), Item(80), Item(86), Item(81)],
    operation_function=lambda x: x * x,
    test_function=lambda x: 0 if x % 11 == 0 else 4,
)

monkeys = [monkey_0, monkey_1, monkey_2, monkey_3, monkey_4, monkey_5, monkey_6, monkey_7]

for i in range(10000):
    print(f'i = {i}')
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspect(item)
            receiving_monkey_idx = monkey.test_item(item)
            monkey.throw_item(item, monkeys[receiving_monkey_idx])
        monkey.remove_all_items()


inspection_numbers = [monkey.num_inspections for monkey in monkeys]
inspection_numbers.sort(reverse=True)
print(f'Monkey business score = {inspection_numbers[0] * inspection_numbers[1]}')
