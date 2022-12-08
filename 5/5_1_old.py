import csv
import pandas as pd


stacks = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}


short_indices = [1, 5, 9, 13, 17, 21, 25, 29]
long_indices = [1, 5, 9, 13, 17, 21, 25, 29, 33]

with open('stacks.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if len(row[0]) == 31:
            for stack_nb, index in enumerate(short_indices, start=1):
                letter = row[0][index]
                stacks[stack_nb].append(letter)
        else:
            for stack_nb, index in enumerate(long_indices, start=1):
                letter = row[0][index]
                stacks[stack_nb].append(letter)

#         stack_row = {}
#         idx = 0
#         word = ''
#         white_space = False
#         for letter in row[0]:
#             if white_space:
#                 continue
#             if letter != ' ':
#                 word += letter
#             else:
#                 word += 'X'
#             print(f'word = {word}')
#             if len(word) == 3:
#                 white_space = True
#                 stack_row[idx] = word
#                 word = ''
#                 idx += 1
