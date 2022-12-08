import csv
from dataclasses import dataclass


@dataclass
class Range:
    lower: int
    upper: int


def get_range(range_string: str) -> Range:
    range_list = range_string.split('-')
    return Range(int(range_list[0]), int(range_list[1]))


def is_total_overlap(range_1: Range, range_2: Range) -> bool:
    return (
            range_1.lower >= range_2.lower and range_1.upper <= range_2.upper
            or range_2.lower >= range_1.lower and range_2.upper <= range_1.upper
    )


total_overlapping_pairs = 0
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        first_range = get_range(row[0])
        second_range = get_range(row[1])
        if is_total_overlap(first_range, second_range):
            total_overlapping_pairs += 1

print(f'Total overlapping pairs = {total_overlapping_pairs}')
