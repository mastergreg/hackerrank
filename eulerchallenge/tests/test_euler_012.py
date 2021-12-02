from unittest import TestCase
from euler_12 import solve, divisors, sieve
from parameterized import parameterized


class TestEuler12(TestCase):
    @parameterized.expand(
        [
            (
                1,
                3,
            ),
            (
                2,
                6,
            ),
            (
                3,
                6,
            ),
            (
                4,
                28,
            ),
        ]
    )
    def test_solve(self, x, expected):
        s = solve(x)
        self.assertEqual(s, expected)

    @parameterized.expand(
        [
            (1, 1),
            (2, 2),
            (3, 2),
            (4, 3),
            (5, 2),
            (6, 4),
            (28, 6),
            (64, 7),
        ]
    )
    def test_divisors(self, x, expected):
        sieve()
        d = divisors(x)
        self.assertEqual(d, expected)
