#!/usr/bin/env python

"""
Largest Sum Contiguous Subarray
description: https://en.wikipedia.org/wiki/Maximum_subarray_problem
"""

def maxContiguousSum(arr):
    current_max_sum = arr[0]
    global_max_sum = arr[0]

    for item in arr[1:]:
        current_max_sum = _max(current_max_sum + item, item)
        if current_max_sum > global_max_sum:
            global_max_sum = current_max_sum

    return global_max_sum

def _max(a, b):
    return a if a >= b else b


if __name__ == "__main__":
    test = [-2, -3, 4, -1, -2, 1, 5, -3]
    print maxContiguousSum(test)
