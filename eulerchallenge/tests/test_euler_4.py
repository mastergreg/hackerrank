from unittest import TestCase
from euler_4 import solve
from parameterized import parameterized


class TestEuler4(TestCase):
    @parameterized.expand(
        [
            (101110, 101101),
            (800000, 793397),
        ]
    )
    def test_solve(self, x, expected):
        s = solve(x)
        self.assertEqual(s, expected)
