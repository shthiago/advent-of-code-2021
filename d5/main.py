import re
from typing import List, Tuple
from collections import namedtuple

Board = List[List[int]]
Point = namedtuple('Point', ['x', 'y'])
Line = Tuple[Point, Point]


def mount_board(h: int, w: int) -> Board:
    return [[0 for _ in range(w)] for __ in range(h)]


def split_raw(raw_input: str) -> List[Tuple[int, int, int, int]]:
    rgx = re.compile(r'\d+')
    rows = [row for row in raw_input.split('\n') if row]
    return list(map(lambda row: tuple([int(v) for v in rgx.findall(row)]),
                    rows))


def parse_lines(raw_input: str) -> List[Line]:
    """Take raw input and return list of Lines"""
    return [(Point(x1, y1), Point(x2, y2))
            for x1, y1, x2, y2 in split_raw(raw_input)]


def draw_in_y(board: Board, start: Point, end: Point) -> Board:
    for y in range(start.y, end.y+1):
        board[y][start.x] += 1
    return board


def draw_in_x(board: Board, start: Point, end: Point) -> Board:
    for x in range(start.x, end.x+1):
        board[start.y][x] += 1
    return board


def draw_diagonal(board: Board, p1: Point, p2: Point) -> Board:
    if p1.x > p2.x:
        seq_x = range(p2.x, p1.x+1)

        if p1.y > p2.y:
            seq_y = range(p2.y, p1.y+1)
        else:
            seq_y = range(p2.y, p1.y-1, -1)

    else:
        seq_x = range(p1.x, p2.x+1)

        if p2.y > p1.y:
            seq_y = range(p1.y, p2.y+1)
        else:
            seq_y = range(p1.y, p2.y-1, -1)

    for x, y in zip(seq_x, seq_y):
        board[y][x] += 1

    return board


def draw_line(board: Board, line: Line):
    """Increment values"""
    p1, p2 = line
    if p1.x == p2.x:
        if p1.y > p2.y:
            return draw_in_y(board, p2, p1)
        else:
            return draw_in_y(board, p1, p2)

    elif p1.y == p2.y:
        if p1.x > p2.x:
            return draw_in_x(board, p2, p1)
        else:
            return draw_in_x(board, p1, p2)

    else:
        return draw_diagonal(board, p1, p2)

    return board


def draw_lines(board: Board, lines: List[Line]) -> Board:
    for line in lines:
        board = draw_line(board, line)

    return board


def main():
    with open('input.txt') as fp:
        lines = parse_lines(fp.read())

    board_h = max([p1.y for p1, _ in lines] + [p2.y for _, p2 in lines]) + 1
    board_w = max([p1.x for p1, _ in lines] + [p2.x for _, p2 in lines]) + 1

    board = draw_lines(mount_board(board_h, board_w), lines)

    flatten = []
    for row in board:
        flatten.extend(row)

    print(f"Total crosses: {len(list(filter(lambda k: k > 1, flatten)))}")


if __name__ == '__main__':
    main()
