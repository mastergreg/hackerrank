from unittest import TestCase
from euler_1 import calc_sum, calc_sum_multiples_3_5, calc_sum_slow
from parameterized import parameterized


class TestEuler1CalcSum(TestCase):
    @parameterized.expand(
        [
            (10, 3),
            (10, 5),
            (100, 5),
            (100, 3),
            (0, 3),
            (100000000, 3),
        ]
    )
    def test_calc_sum(self, maximum, d):
        expected = calc_sum_slow(maximum, d)
        s = calc_sum(maximum, d)
        self.assertEqual(s, expected)


class TestEuler1CalcSumMultiples35(TestCase):
    @parameterized.expand(
        [
            (10, 23),
            (100, 2318),
        ]
    )
    def test_calc_sum_multiples_3_5(self, maximum, expected):
        s = calc_sum_multiples_3_5(maximum)
        self.assertEqual(s, expected)
