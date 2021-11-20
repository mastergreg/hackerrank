#!/usr/bin/python


def fib(n, fibdict):
    r = fibdict.get(n)
    if r:
        return r
    else:
        fibdict[n] = fibdict[n - 1] + fibdict[n - 2]
        r = fibdict[n]
        return r


def solve(x):
    fibdict = {1: 1, 2: 2}
    even = []
    for i in range(1, x):
        fibdict[i] = fib(i, fibdict)
        if fibdict[i] >= x:
            break
        if fibdict[i] % 2 == 0:
            even.append(fibdict[i])

    return sum(even)


def main():
    n = int(input().strip())
    for _ in range(n):
        n = int(input().strip())
        print(solve(n))


if __name__ == "__main__":
    main()
