from unittest import TestCase
from euler_9 import solve, solve_slow
from parameterized import parameterized


class TestEuler9(TestCase):
    @parameterized.expand(
        [
            (12, 60),
            (4, -1),
            (5, -1),
            (36, 1620),
            (19, -1),
        ]
    )
    def test_solve(self, x, expected):
        s = solve(x)
        self.assertEqual(s, expected)
