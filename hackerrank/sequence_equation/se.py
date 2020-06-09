#!/bin/python3

import os


# Complete the permutationEquation function below.
def permutation_equation(p):
    vals = []
    for x in range(1, len(p) + 1):
        for y in p:
            if p[p[y - 1] - 1] == x:
                vals.append(y)
                break
    return vals


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutation_equation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
