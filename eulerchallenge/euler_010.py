#!/usr/bin/python3
from bisect import bisect_right

N = 1000000 + 1
SIEVE = set(list(range(3, N, 2)))
SIEVE.add(2)

SIEVE_LIST = list()
SUM_LOOKUP = {}


def get_sum(x):
    ret = 0
    for i in SIEVE_LIST:
        if i <= x:
            ret += i
        else:
            return ret


def get_sum_bisect(x):
    i = bisect_right(SIEVE_LIST, x)
    return sum(SIEVE_LIST[:i])


def get_sum_bisect_lookup(x):
    i = bisect_right(SIEVE_LIST, x)
    return SUM_LOOKUP[i - 1]


def solve(x):
    tot = 0
    ret = get_sum_bisect_lookup(x)
    return ret


def sieve():
    global SIEVE_LIST
    for i in range(3, N, 2):
        for j in range(i + i, N, i):
            SIEVE.discard(j)
    SIEVE_LIST = sorted(list(SIEVE))
    SUM_LOOKUP[-1] = 0
    for i, prime in enumerate(SIEVE_LIST):
        SUM_LOOKUP[i] = prime + SUM_LOOKUP[i - 1]


def main():
    sieve()
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(solve(n))


if __name__ == "__main__":
    main()
