#!/bin/python3

import os


# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    days = 0
    for x in range(i, j + 1):
        x_s = str(x)
        x_s_rev = reverse_val(x_s)
        if abs(x - x_s_rev) % k == 0:
            days += 1
    return days


def reverse_val(x_s) -> int:
    idx = len(x_s) - 1
    non_zero_found = False
    x_s_rev = ''
    while idx >= 0:
        if x_s[idx] == 0 and not non_zero_found:
            non_zero_found = True
            idx -= 1
            continue
        x_s_rev += x_s[idx]
        idx -= 1
    print(f'Reversed {x_s} as {int(x_s_rev)}')
    return int(x_s_rev)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
