import csv
from dataclasses import dataclass


@dataclass
class Weapon:
    type: str
    points: int
    beats: int


rock = Weapon('Rock', points=1, beats=3)
paper = Weapon('Paper', points=2, beats=1)
scissors = Weapon('Scissors', points=3, beats=2)

weapons_lookup = {
    'A': rock,
    'B': paper,
    'C': scissors,
    'X': rock,
    'Y': paper,
    'Z': scissors,
}


def get_points(opponent: Weapon, my: Weapon) -> int:
    if my.points == opponent.points:
        return 3 + my.points
    elif opponent.points == my.beats:
        return 6 + my.points
    else:
        return my.points


total_points = 0
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        opponent_choice = weapons_lookup[row[0][0]]
        my_choice = weapons_lookup[row[0][2]]
        points = get_points(opponent_choice, my_choice)
        total_points += points

print(f'Total points = {total_points}')
