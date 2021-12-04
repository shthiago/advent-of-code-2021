# Day 2
# https://adventofcode.com/2021/day/2

final_x = 0
final_y = 0


class Submarine:
    def __init__(self):
        self.x = 0
        self.depth = 0
        self.aim = 0

        self.cmds = {
            'up': self.up,
            'down': self.down,
            'forward': self.forward
        }

    def down(self, d: int):
        self.aim += d

    def up(self, d: int):
        self.aim -= d

    def forward(self, d: int):
        self.x += d
        self.depth += self.aim * d

    def __getitem__(self, name):
        return self.cmds[name]


if __name__ == '__main__':
    submarine = Submarine()
    with open('input.txt') as fp:
        for row in fp:
            cmd, value = row.split()
            value = int(value)

            submarine[cmd](value)

    print(f"Submarine is at: ({submarine.x}, {submarine.depth})")
    print(f"Result is: {submarine.x * submarine.depth}")
