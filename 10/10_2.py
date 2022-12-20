import csv


str_row = '........................................'


class Sprite:
    def __init__(self, center_position: int):
        self.center_position = center_position
        self.string_row = ''

    def in_sprite(self, _cycle: int) -> bool:
        return _cycle in self._get_positions()

    def update_center_position(self, offset: int) -> None:
        self.center_position += offset

    def set_center_position(self, position: int) -> None:
        self.center_position = position

    def _get_positions(self) -> list[int]:
        return [self.center_position - 1, self.center_position, self.center_position + 1]


cycle = 1
register = 1

sprite = Sprite(1)

with open("input.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        str_row = str_row[:register] + '###' + str_row[register+3:]
        print(str_row)
        if row[0] == 'noop':
            if sprite.in_sprite(cycle):
                sprite.string_row += '#'
            else:
                sprite.string_row += '.'
            cycle += 1
        else:
            if sprite.in_sprite(cycle):
                sprite.string_row += '#'
            else:
                sprite.string_row += '.'
            cycle += 1
            if sprite.in_sprite(cycle):
                sprite.string_row += '#'
            else:
                sprite.string_row += '.'
            cycle += 1
            register += int(row[0].split(' ')[1])
            sprite.set_center_position(register)
