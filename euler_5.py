#!/usr/bin/python
SOLUTIONS = {}


def is_evenly_divisibile_by(x, i):
    return x % i == 0


def solve(x):
    tmp = SOLUTIONS.get(x, None)
    if tmp is not None:
        return tmp
    domain = list(range(1, x + 1))
    for i in range(1, 10000000):
        all_divisions = (is_evenly_divisibile_by(i, j) for j in domain)
        if all(all_divisions):
            return i


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        SOLUTIONS[n] = solve(n)
        print(SOLUTIONS[n])


if __name__ == "__main__":
    main()
