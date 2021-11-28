#!/usr/bin/python
SOLUTIONS = {}


def is_palindrome(x):
    lx = list(str(x))
    rlx = list(lx)
    rlx.reverse()
    return lx == rlx


def solve(x):
    tmp = SOLUTIONS.get(x, None)
    if tmp is not None:
        return tmp
    ret = 101101
    for i in range(100, 1000):
        for j in range(100, 1000):
            test = i * j
            if test >= x:
                break
            if test <= ret:
                continue
            if is_palindrome(test):
                ret = max(ret, test)
    return ret


def main():
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        SOLUTIONS[n] = solve(n)
        print(SOLUTIONS[n])


if __name__ == "__main__":
    main()
