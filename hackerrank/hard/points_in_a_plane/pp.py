#!/bin/python3

import os
from typing import List


def points_in_plane(coordinates):
    """


    :param coordinates: List of pairs of coordinates
    :return:
    """

    # Catalog all points into lists that contain the same x or y coordinate.
    # This will help determine the next largest set of coordinates that can be removed.
    #
    # Example:
    # X-Coordinates list will contain all pairs that have the same x coordinate.  The data structure
    # will be a list of lists, with the index of the outer list representing the x coordinate value of
    # the pairs inside that list.
    # [
    #   [1, 2, 3, 4]   - The following pairs = (0, 1), (0, 2), (0, 3), (0, 4)
    #   [4, 6]         - The following pairs = (1, 4), (1, 6)
    # ]
    #
    # Same will be done for Y

    # Sweep through coordinates to find largest x and y coordinates so we can set up our lists
    turns: int = determine_min_turns(coordinates)

    return [turns, 0]


def determine_min_turns(coordinates: List[List[int]]) -> int:
    max_x = None
    max_y = None
    for c in coordinates:
        if max_x is None or max_x < c[0]:
            max_x = c[0]
        if max_y is None or max_y < c[1]:
            max_y = c[1]
    x_lookup = [[] for _ in range(0, max_x + 1)]
    y_lookup = [[] for _ in range(0, max_y + 1)]
    for c in coordinates:
        # Put the y-coordinate in the list at index [x-coordinate]
        x_lookup[c[0]].append(c)
        # Put the x-coordinate in the list at index [y-coordinate]
        y_lookup[c[1]].append(c)
    # Now that all the pairs are cataloged, let's sort the lists in each look-up so the largest is first.
    x_lookup.sort(key=lambda x: len(x), reverse=True)
    y_lookup.sort(key=lambda x: len(x), reverse=True)
    remaining = {f'{c[0]}-{c[1]}' for c in coordinates}
    processed = set()
    turns = 0
    while remaining:
        # Choose largest remaining list from x and y
        if len(x_lookup[0]) > len(y_lookup[0]):
            process_list(processed, remaining, x_lookup)
        else:
            process_list(processed, remaining, y_lookup)
        turns += 1
    return turns


def process_list(processed, remaining, lookup):
    for v in lookup[0]:
        key = f'{v[0]}-{v[1]}'
        remaining.discard(key)
        processed.add(key)
    del lookup[0]


def process():
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())

        coordinates = []

        for _ in range(n):
            coordinates.append(list(map(int, input().rstrip().split())))

        result = points_in_plane(coordinates)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')
    fptr.close()


if __name__ == '__main__':
    process()
