from unittest import TestCase
from euler_7 import solve, sieve
from parameterized import parameterized


class TestEuler6(TestCase):
    @parameterized.expand(
        [
            (3, 5),
            (6, 13),
        ]
    )
    def test_solve(self, x, expected):
        sieve()
        s = solve(x)
        self.assertEqual(s, expected)

    def test_limit(self):
        sieve()
        for x in range(1, 10001):
            solve(x)
