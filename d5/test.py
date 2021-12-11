import unittest

from main import *


class DayFiveTests(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_board_creation(self):
        self.assertEqual(mount_board(1, 1), [[0]])
        self.assertEqual(mount_board(2, 2), [[0, 0], [0, 0]])

    def test_split_raw(self):
        raw_input = "1,2 -> 3,4\n5,6 -> 7,8"
        self.assertEqual([(1, 2, 3, 4), (5, 6, 7, 8)],
                         split_raw(raw_input))

    def test_parse_lines(self):
        raw_input = "1,2 -> 3,4\n5,6 -> 7,8"
        self.assertEqual([((1, 2), (3, 4)), ((5, 6), (7, 8))],
                         parse_lines(raw_input))

    def test_draw_in_x(self):
        board = [[0, 0], [0, 0]]
        start = Point(0, 0)
        end = Point(1, 0)
        expected = [[1, 1], [0, 0]]
        self.assertEqual(expected, draw_in_x(board, start, end))

    def test_draw_in_y(self):
        board = [[0, 0], [0, 0], [0, 0]]
        start = Point(0, 0)
        end = Point(0, 1)
        expected = [[1, 0], [1, 0], [0, 0]]
        self.assertEqual(expected, draw_in_y(board, start, end))

    def test_draw_in_diagonal_main_diag(self):
        board = mount_board(5, 5)
        start = Point(0, 0)
        end = Point(4, 4)
        expected = [[1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 1, 0, 0],
                    [0, 0, 0, 1, 0],
                    [0, 0, 0, 0, 1]]

        drawn_board = draw_diagonal(board, start, end)

        self.assertEqual(expected, drawn_board)

    def test_draw_in_diagonal_secondary_diag(self):
        board = mount_board(5, 5)
        start = Point(4, 0)
        end = Point(0, 4)
        expected = [[0, 0, 0, 0, 1],
                    [0, 0, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 0, 0],
                    [1, 0, 0, 0, 0]]

        drawn_board = draw_diagonal(board, start, end)

        self.assertEqual(expected, drawn_board)

    def test_draw_lines(self):
        lines = [(Point(0, 9), Point(5, 9)),
                 (Point(8, 0), Point(0, 8)),
                 (Point(9, 4), Point(3, 4)),
                 (Point(2, 2), Point(2, 1)),
                 (Point(7, 0), Point(7, 4)),
                 (Point(6, 4), Point(2, 0)),
                 (Point(0, 9), Point(2, 9)),
                 (Point(3, 4), Point(1, 4)),
                 (Point(0, 0), Point(8, 8)),
                 (Point(5, 5), Point(8, 2))]

        board = mount_board(10, 10)

        expected = [[1, 0, 1, 0, 0, 0, 0, 1, 1, 0],
                    [0, 1, 1, 1, 0, 0, 0, 2, 0, 0],
                    [0, 0, 2, 0, 1, 0, 1, 1, 1, 0],
                    [0, 0, 0, 1, 0, 2, 0, 2, 0, 0],
                    [0, 1, 1, 2, 3, 1, 3, 2, 1, 1],
                    [0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                    [2, 2, 2, 1, 1, 1, 0, 0, 0, 0]]

        drawn_board = draw_lines(board, lines)
        self.assertEqual(expected, drawn_board)
