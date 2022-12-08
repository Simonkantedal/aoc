import csv
from dataclasses import dataclass


@dataclass
class TopThreeElves:
    first: int = 0
    second: int = 0
    third: int = 0


top_three_elves = TopThreeElves()
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    calories = 0
    for row in csv_reader:
        if row:
            calories += int(row[0])
        else:
            calories = 0
        if calories > top_three_elves.first:
            top_three_elves.first = calories
        elif calories > top_three_elves.second:
            top_three_elves.second = calories
        elif calories > top_three_elves.third:
            top_three_elves.third = calories

print(f'Most calories = {top_three_elves.first}')
print(f'Second most calories = {top_three_elves.second}')
print(f'Third most calories = {top_three_elves.third}')
print(f'Sum of top three = {top_three_elves.first + top_three_elves.second + top_three_elves.third}')
