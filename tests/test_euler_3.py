from unittest import TestCase
from euler_3 import solve, max_divide
from parameterized import parameterized


class TestEuler3(TestCase):
    @parameterized.expand(
        [
            (10, 5),
            (17, 17),
        ]
    )
    def test_solve(self, x, expected):
        s = solve(x)
        self.assertEqual(s, expected)

    @parameterized.expand(
        [
            (10, 2, 5),
            (17, 2, 17),
        ]
    )
    def test_max_divide(self, x, a, expected):
        s = max_divide(x, a)
        self.assertEqual(s, expected)
