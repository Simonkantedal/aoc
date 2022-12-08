import csv
import string

letters = string.ascii_lowercase + string.ascii_uppercase

priorities = {letter: priority for priority, letter in enumerate(letters, start=1)}


def find_common_letter(string_1: str, string_2: str, string_3: str) -> str:
    for letter in string_1:
        if letter in string_2 and letter in string_3:
            return letter


sum_of_priorities = 0
with open('input.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    string_triplet = []
    for idx, row in enumerate(csv_reader, start=1):
        string_triplet.append(row[0])
        if idx % 3 == 0.0:
            common_letter = find_common_letter(string_triplet[0], string_triplet[1], string_triplet[2])
            sum_of_priorities += priorities[common_letter]
            string_triplet = []

print(f'Sum of priorities = {sum_of_priorities}')
