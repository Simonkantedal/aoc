import csv
from dataclasses import dataclass


@dataclass
class Range:
    lower: int
    upper: int


def get_range(range_string: str) -> Range:
    range_list = range_string.split('-')
    return Range(int(range_list[0]), int(range_list[1]))


def is_any_overlap(range_1: Range, range_2: Range) -> bool:
    return not (range_1.upper < range_2.lower or range_1.lower > range_2.upper)


at_all_overlapping_pairs = 0
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        first_range = get_range(row[0])
        second_range = get_range(row[1])
        if is_any_overlap(first_range, second_range):
            at_all_overlapping_pairs += 1

print(f'At all overlapping pairs = {at_all_overlapping_pairs}')
