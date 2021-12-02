#!/usr/bin/python
import math


def max_divide(x, a):
    r = 0
    qi = x
    while r == 0 and qi > 1:
        q = qi
        qi, r = divmod(q, a)
    return q


SOLUTIONS = {}


def solve(x):
    tmp = SOLUTIONS.get(x, None)
    if tmp is not None:
        return tmp
    xi = max_divide(x, 2)
    max_range = math.sqrt(xi) + 1
    i = 3
    while i <= max_range:
        ans = max_divide(xi, i)
        if ans == 1:
            return i
        else:
            xi = ans
            max_range = math.sqrt(xi) + 1
        i += 2
    return xi


def main():
    n = int(input().strip())
    for _ in range(n):
        n = int(input().strip())
        SOLUTIONS[n] = solve(n)
        print(SOLUTIONS[n])


if __name__ == "__main__":
    main()
