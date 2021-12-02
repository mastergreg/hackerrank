from unittest import TestCase
from euler_5 import solve
from parameterized import parameterized


class TestEuler5(TestCase):
    @parameterized.expand(
        [
            (3, 6),
            (10, 2520),
        ]
    )
    def test_solve(self, x, expected):
        s = solve(x)
        self.assertEqual(s, expected)
