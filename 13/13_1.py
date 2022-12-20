import ast
import csv
from dataclasses import dataclass


@dataclass
class Pair:
    left: list | int | None
    right: list | int | None


def evaluate_pair(current_pair: Pair, status: bool) -> bool | None:
    if isinstance(current_pair.left, int) and isinstance(current_pair.right, int):
        if current_pair.left < current_pair.right:
            return True
        elif current_pair.left > current_pair.right:
            return False
        else:
            return None

    elif isinstance(current_pair.left, list) and isinstance(current_pair.right, int):
        left_list = current_pair.left
        right_list = [current_pair.right]
        new_pair = Pair(left_list, right_list)
        if evaluate_pair(new_pair, status) is not None:
            return evaluate_pair(new_pair, status)

    elif isinstance(current_pair.left, int) and isinstance(current_pair.right, list):
        left_list = [current_pair.left]
        right_list = current_pair.right
        new_pair = Pair(left_list, right_list)
        if evaluate_pair(new_pair, status) is not None:
            return evaluate_pair(new_pair, status)

    elif isinstance(current_pair.left, list) and isinstance(current_pair.right, list):
        for idx in range(max(len(current_pair.left), len(current_pair.right))):
            try:
                left_item = current_pair.left[idx]
            except BaseException:
                return True
            try:
                right_item = current_pair.right[idx]
            except BaseException:
                return False
            new_pair = Pair(left_item, right_item)
            if evaluate_pair(new_pair, status) is not None:
                return evaluate_pair(new_pair, status)


    if isinstance(current_pair.left, list) and isinstance(current_pair.right, list):
        if len(current_pair.left) < len(current_pair.right):
            status = True
        elif len(current_pair.left) > len(current_pair.right):
            status = False
        else:
            for idx, left_item in enumerate(current_pair.left):
                right_item = current_pair.right[idx]
                new_pair = Pair(left_item, right_item)
                status = evaluate_pair(new_pair, status)
    return status


pairs = []
with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';', quotechar='|')
    pair = Pair(left=None, right=None)
    for row in csv_reader:
        if not row:
            pair = Pair(left=None, right=None)
            continue
        if pair.left is None:
            pair.left = ast.literal_eval(str(row[0]))
        elif pair.right is None:
            pair.right = ast.literal_eval(str(row[0]))
            pairs.append(pair)


total_sum = 0
for idx, _pair in enumerate(pairs, start=1):
    print(f'{_pair}: {evaluate_pair(_pair, status=False)}')
    if evaluate_pair(_pair, status=False):
        total_sum += idx

print(f'Total sum = {total_sum}')
