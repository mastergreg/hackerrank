#!/bin/python3

import sys


def arithmetic_progression_sum(a0, an, n):
    return (a0 + an) * n >> 1


def calc_sum(maximum, d):
    a0 = d

    if d > maximum:
        return 0
    n = maximum // d
    an = n * d

    if an == maximum:
        an -= d
        n -= 1

    return arithmetic_progression_sum(a0, an, n)


def calc_sum_slow(maximum, d):
    a = 0
    for x in range(d, maximum, d):
        a += x
    return a


def calc_sum_multiples_3_5(n):
    s1 = calc_sum(n, 3)
    s2 = calc_sum(n, 5)
    s3 = calc_sum(n, 15)
    return int(s1 + s2 - s3)


def main():
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(calc_sum_multiples_3_5(n))


if __name__ == "__main__":
    main()
