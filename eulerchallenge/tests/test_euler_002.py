from unittest import TestCase
from euler_2 import fib, solve
from parameterized import parameterized


class TestEuler2(TestCase):
    @parameterized.expand(
        [
            (10, 10),
            (100, 44),
        ]
    )
    def test_solve(self, x, expected):
        s = solve(x)
        self.assertEqual(s, expected)
