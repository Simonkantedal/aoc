import csv
import string

letters = string.ascii_lowercase + string.ascii_uppercase

priorities = {letter: priority for priority, letter in enumerate(letters, start=1)}


def split_string(input_string: str) -> tuple[str, str]:
    string_length = len(input_string)
    string_1 = input_string[:int(string_length/2)]
    string_2 = input_string[int(string_length/2):]
    return string_1, string_2


def find_common_letter(string_1: str, string_2: str) -> str:
    for letter in string_1:
        if letter in string_2:
            return letter


sum_of_priorities = 0
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        str_1, str_2 = split_string(row[0])
        common_letter = find_common_letter(str_1, str_2)
        sum_of_priorities += priorities[common_letter]
        print(f'String 1 = {str_1}, String 2 = {str_2}, Common letter = {common_letter}')

print(f'Sum of priorities = {sum_of_priorities}')