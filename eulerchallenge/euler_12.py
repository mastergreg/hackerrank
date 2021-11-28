#!/usr/bin/python3
from math import ceil, sqrt

N = 1000 + 1
SIEVE = set(list(range(3, N, 2)))
SIEVE.add(2)
SIEVE_LIST = []

DIVISORS = {}
SOLVE = {}


def gen_triangle():
    MAX_LOOP = 1000000000
    t = 1
    x = 0
    while t < MAX_LOOP:
        x += t
        t += 1
        yield x


def get_triangle(n):
    return int((n + 1) * n / 2)


def sieve():
    global SIEVE_LIST
    for i in range(3, N, 2):
        for j in range(i + i, N, i):
            SIEVE.discard(j)
    SIEVE_LIST = sorted(list(SIEVE))


DIV_CACHE = {}

DIV_CACHE_SET = {}


def divisors_slow(x):
    initial = x
    if x == 1:
        return 1
    sqr = sqrt(x)
    max_i = ceil(sqr)
    d = 1
    for prime in SIEVE_LIST:
        power = 0
        if DIV_CACHE.get(x, 0) > 0:
            d *= DIV_CACHE[x]
            DIV_CACHE[initial] = d
            return d
        newx, mod = divmod(x, prime)
        while mod == 0:
            power += 1
            x = newx
            newx, mod = divmod(x, prime)
        d *= power + 1
        if prime > max_i:
            break
    DIV_CACHE[initial] = d
    return d

def divisors(x):
    initial = x
    if x == 1:
        return 1
    sqr = sqrt(x)
    max_i = ceil(sqr)
    for prime in SIEVE_LIST:


def solve(x):
    sieve()
    t = SOLVE.get(x, None)
    if t is not None:
        return t
    prod = x
    # i = 1
    # triangle = get_triangle(i)
    # while divisors(triangle) <= x:
    #     i += 1
    #     triangle = get_triangle(i)
    for triangle in gen_triangle():
        if divisors(triangle) > x:
            SOLVE[x] = triangle
            return triangle


def main():
    for _ in range(int(input())):
        n = int(input())
        s = solve(n)
        print(s)


if __name__ == "__main__":
    main()
