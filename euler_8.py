#!/usr/bin/python
SOLUTIONS = {}


def get_digit_lists(x, number):
    digit_list = list(map(int, str(number)))
    ret = []
    for i in range(len(digit_list) - x + 1):
        tmp_list = digit_list[i : i + x]
        ret.append(tmp_list)
    return ret


def prod(x):
    prd = 1
    for i in x:
        prd *= i
    return prd


def solve(x, number):
    tmp = SOLUTIONS.get(x, None)
    if tmp is not None:
        return tmp

    digit_lists = get_digit_lists(x, number)
    prd = 0
    for digit_list in digit_lists:
        prd = max(prd, prod(digit_list))

    ret = prd
    return ret


def main():
    t = int(input().strip())
    for _ in range(t):
        digits, n = map(int, input().split())
        number = int(input().strip())
        SOLUTIONS[number] = solve(n, number)
        print(SOLUTIONS[number])


if __name__ == "__main__":
    main()
