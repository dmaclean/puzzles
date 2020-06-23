#!/bin/python3

import os


# Complete the workbook function below.
def workbook(n, k, arr):
    special = 0
    curr_page = 1
    for idx in range(1, n + 1):
        num_problems = arr[idx - 1]
        print(f'Number of problems for chapter {idx} is {num_problems}')
        pages = (num_problems // k) + (1 if num_problems % k > 0 else 0)

        for p in range(1, num_problems + 1):
            page_num = curr_page + ((p - 1) // k)
            if page_num == p:
                print(f'Problem {p} is on page {page_num}')
                special += 1

        curr_page += pages
    return special


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
