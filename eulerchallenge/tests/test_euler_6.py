from unittest import TestCase
from euler_6 import solve, square_sum, sum_square
from parameterized import parameterized


class TestEuler6(TestCase):
    def test_square_sum(self):
        s = square_sum(10)
        self.assertEqual(s, 3025)

    def test_sum_square(self):
        s = sum_square(10)
        self.assertEqual(s, 385)

    @parameterized.expand(
        [
            (3, 22),
            (10, 2640),
        ]
    )
    def test_solve(self, x, expected):
        s = solve(x)
        self.assertEqual(s, expected)
