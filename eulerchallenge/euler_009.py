#!/usr/bin/python
from math import ceil


def get_triplet_slow(x):
    amax = (x + 1) // 2
    bmax = (x + 1) // 2
    for a in range(1, amax):
        for b in range(a + 1, bmax):
            if a + b > x:
                break
            c = x - a - b
            if is_pythagorean(a, b, c):
                yield (a, b, c)


def get_triple_euler_non_inclusive(x):
    c = 0
    m = 2
    while c < 3 * x:
        for n in range(1, m):
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            tot = 2 * m * n + 2 * m * m
            if tot == x:
                a = m * m - n * n
                b = 2 * m * n
                c = m * m + n * n
                yield (a, b, c)
        m += 1


def get_triplet_dickinson(x):

    rmax = ceil(x / 3)
    for r in range(1, rmax):
        rsq = r * r
        for s in range(1, x - 3 * r):
            t = rsq / (2 * s)
            if t.is_integer() and t > s:
                t = int(t)
                # if rsq == 2 * s * t:
                a = r + s
                b = r + t
                c = r + s + t

                tot = a + b + c
                if tot == x:
                    yield (a, b, c)


def get_triplet(x):
    return get_triplet_linear(x)


def is_pythagorean(a, b, c):
    return a * a + b * b == c * c


def solve_slow(x):
    ret = -1
    for a, b, c in get_triplet_slow(x):
        ret = max(ret, a * b * c)
    if ret == 0:
        ret = -1
    return ret


def get_triplet_linear(x):
    for a in range(1, x):
        b = get_b(x, a)
        c = x - a - b
        if is_pythagorean(a, b, c):
            yield (a, b, c)


def get_b(x, a):
    b = (x * x - 2 * x * a) / (2 * x - 2 * a)
    return int(b)


def solve(x):
    ret = -1
    for a, b, c in get_triplet(x):
        ret = max(ret, a * b * c)
    if ret == 0:
        ret = -1
    return ret


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(solve(n))


def test_both():
    solve(13)
    for i in range(1, 3001):
        s1 = solve(i)
        s2 = solve_slow(i)
        if s1 != s2:
            print(i, s2)


if __name__ == "__main__":
    main()
