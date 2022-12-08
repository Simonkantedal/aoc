import csv
from dataclasses import dataclass


@dataclass
class Weapon:
    type: str
    points: int
    opponents_winning_points: int
    opponents_losing_points: int


rock = Weapon('Rock', points=1, opponents_winning_points=2, opponents_losing_points=3)
paper = Weapon('Paper', points=2, opponents_winning_points=3, opponents_losing_points=1)
scissors = Weapon('Scissors', points=3, opponents_winning_points=1, opponents_losing_points=2)

weapons_lookup = {
    'A': rock,
    'B': paper,
    'C': scissors,
}


def get_points(opponent: Weapon, expected_result: str) -> int:
    if expected_result == 'Z':
        return 6 + opponent.opponents_winning_points
    elif expected_result == 'Y':
        return 3 + opponent.points
    elif expected_result == 'X':
        return opponent.opponents_losing_points


total_points = 0
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        opponent_weapon = weapons_lookup[row[0][0]]
        expected_result = row[0][2]
        points = get_points(opponent=opponent_weapon, expected_result=expected_result)
        print(f'Opponent weapon = {opponent_weapon}, Expected result = {expected_result}, Points = {points}')
        total_points += points

print(f'Total points = {total_points}')
