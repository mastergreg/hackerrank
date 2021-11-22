from unittest import TestCase
from euler_8 import solve, get_digit_lists
from parameterized import parameterized


class TestEuler8(TestCase):
    @parameterized.expand(
        [
            (5, 3675356291, 3150),
            (5, 2709360626, 0),
        ]
    )
    def test_solve(self, x, number, expected):
        s = solve(x, number)
        self.assertEqual(s, expected)

    @parameterized.expand(
        [
            (
                5,
                3675356291,
                [
                    [3, 6, 7, 5, 3],
                    [6, 7, 5, 3, 5],
                    [7, 5, 3, 5, 6],
                    [5, 3, 5, 6, 2],
                    [3, 5, 6, 2, 9],
                    [5, 6, 2, 9, 1],
                ],
            ),
            (
                5,
                2709360626,
                [
                    [2, 7, 0, 9, 3],
                    [7, 0, 9, 3, 6],
                    [0, 9, 3, 6, 0],
                    [9, 3, 6, 0, 6],
                    [3, 6, 0, 6, 2],
                    [6, 0, 6, 2, 6],
                ],
            ),
        ]
    )
    def test_get_digit_list(self, x, number, expected):
        s = get_digit_lists(x, number)
        self.assertListEqual(s, expected)
