import csv


cycles_of_interest = [20, 60, 100, 140, 180, 220]


cycle = 1
register = 1
signal_strength_sum = 0

with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[0] == 'noop':
            if cycle in cycles_of_interest:
                signal_strength_sum += cycle * register
            cycle += 1
        else:
            if cycle in cycles_of_interest:
                signal_strength_sum += cycle * register
            cycle += 1
            if cycle in cycles_of_interest:
                signal_strength_sum += cycle * register
            cycle += 1
            register += int(row[0].split(' ')[1])

print(signal_strength_sum)
