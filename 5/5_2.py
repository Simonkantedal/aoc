import csv
from dataclasses import dataclass


@dataclass
class Action:
    nb_crates: int
    origin: int
    destination: int


stacks = {
    1: ["D", "T", "W", "N", "L"],
    2: ["H", "P", "C"],
    3: ["J", "M", "G", "D", "N", "H", "P", "W"],
    4: ["L", "Q", "T", "N", "S", "W", "C"],
    5: ["N", "C", "H", "P"],
    6: ["B", "Q", "W", "M", "D", "N", "H", "T"],
    7: ["L", "S", "G", "J", "R", "B", "M"],
    8: ["T", "R", "B", "V", "G", "W", "N", "Z"],
    9: ["L", "P", "N", "D", "G", "W"],
}


def get_action(action_string: str) -> Action:
    nb_crates = int(action_string.split("move ")[1].split(" from")[0])
    origin = int(action_string.split("from ")[1].split(" to")[0])
    destination = int(action_string.split("to ")[1])
    return Action(nb_crates, origin, destination)


def perform_action(_stacks, _action: Action) -> None:
    new_destination_stack = _stacks[_action.origin][:_action.nb_crates] + _stacks[_action.destination]
    _stacks[_action.destination] = new_destination_stack
    for _ in range(_action.nb_crates):
        _stacks[_action.origin].pop(0)


with open("actions.csv") as actions_csv:
    csv_reader = csv.reader(actions_csv)
    for row in csv_reader:
        action = get_action(row[0])
        perform_action(stacks, action)
