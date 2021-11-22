#!/usr/bin/python
SOLUTIONS = {}

N = 1000000 + 1
SIEVE = set(list(range(3, N, 2)))
SIEVE.add(2)

SIEVE_LIST = list()


def solve(x):
    tmp = SOLUTIONS.get(x, None)
    if tmp is not None:
        return tmp
    ret = SIEVE_LIST[x - 1]
    return ret


def sieve():
    global SIEVE_LIST
    for i in range(3, N, 2):
        for j in range(i + i, N, i):
            SIEVE.discard(j)
    SIEVE_LIST = sorted(list(SIEVE))


def main():
    sieve()
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        SOLUTIONS[n] = solve(n)
        print(SOLUTIONS[n])


if __name__ == "__main__":
    main()
