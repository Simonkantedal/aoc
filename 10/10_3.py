import csv


rows = ['', '', '', '', '', '']


def update_cycle(_cycle: int, _row_idx: int, sprite_position: int, _pixel: int):
    if _cycle % 40 == 0:
        _row_idx += 1
        sprite_position = sprite_position % 40
        _pixel = _pixel % 40
    _cycle += 1
    _pixel += 1
    return _cycle, _row_idx, sprite_position, _pixel


def get_character(_pixel: int, sprite_position: int) -> str:
    sprite_range = [sprite_position - 1, sprite_position, sprite_position + 1]
    if _pixel in sprite_range:
        return '#'
    else:
        return '.'


row_idx = 0
pixel = 0
cycle = 1
register = 1
with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        if row[0] == 'noop':
            rows[row_idx] += get_character(pixel, register)
            cycle, row_idx, register, pixel = update_cycle(cycle, row_idx, register, pixel)
        else:
            rows[row_idx] += get_character(pixel, register)
            cycle, row_idx, register, pixel = update_cycle(cycle, row_idx, register, pixel)
            rows[row_idx] += get_character(pixel, register)
            register += int(row[0].split(' ')[1])
            cycle, row_idx, register, pixel = update_cycle(cycle, row_idx, register, pixel)
