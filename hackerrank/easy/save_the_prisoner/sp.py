#!/bin/python3

import os


# Complete the saveThePrisoner function below.
def save_the_prisoner(n, m, s):
    val = ((m % n) + (s - 1))
    if val > n:
        val %= n
    if val == 0:
        val = n
    return val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = save_the_prisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
