#!/usr/bin/python
SOLUTIONS = {}


def square_sum(x):
    return sum(range(1, x + 1)) ** 2


def sum_square(x):
    return sum((i * i for i in range(1, x + 1)))


def solve(x):
    tmp = SOLUTIONS.get(x, None)
    if tmp is not None:
        return tmp
    return square_sum(x) - sum_square(x)


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        SOLUTIONS[n] = solve(n)
        print(SOLUTIONS[n])


if __name__ == "__main__":
    main()
