#!/bin/python3

import os
import time


# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    if not scores:
        return [1 for a in alice]

    # Index this thing
    start = time.time()
    curr_rank = 1
    curr_score = scores[0]
    score_rank = [scores[0]]
    for s in scores:
        if curr_score != s:
            curr_score = s
            curr_rank += 1
            score_rank.append(curr_score)
    print(f'Indexed in {time.time() - start} seconds')

    a_ranks = []
    for a in alice:
        r = 1
        # found = False
        # for i in range(0, len(score_rank)):
        #     sr = score_rank[i]
        #     if a >= sr:
        #         a_ranks.append(i+1)
        #         found = True
        #         break
        # if not found:
        #     a_ranks.append(len(score_rank) + 1)
        a_ranks.append(binary_search(score_rank, a, len(score_rank) - 1, 0))
    return a_ranks


def binary_search(arr, val, h, l):
    if l >= h:
        if val > arr[h] and h <= 0:
            return 1
        elif val > arr[h]:
            return h + 1
        elif val < arr[h]:
            return h + 2
        else:
            return h + 1

    mid = (h + l) // 2
    if arr[mid] == val:
        return mid + 1
    elif val > arr[mid]:
        return binary_search(arr, val, mid - 1, l)
    else:
        return binary_search(arr, val, h, mid + 1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
