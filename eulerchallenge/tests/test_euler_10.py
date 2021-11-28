from unittest import TestCase
from euler_10 import solve, sieve
from parameterized import parameterized


class TestEuler10(TestCase):
    @parameterized.expand(
        [
            (5, 10),
            (10, 17),
            (1, 0),
        ]
    )
    def test_solve(self, x, expected):
        sieve()
        s = solve(x)
        self.assertEqual(s, expected)
