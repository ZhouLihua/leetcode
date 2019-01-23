#! /usr/bin/env python

"""
Given an array containing all the members from 1 to n except 2, find the two missing numbers
eg missing([4, 2, 3]) = 1, 5
"""


def missing_two(arr):
    n = len(arr) + 2
    total_sum = n * (n + 1) / 2
    arr_sum = 0
    for ele in arr:
        arr_sum += ele
    pivot = (total_sum - arr_sum) / 2

    left_xor = 0
    right_xor = 0
    for i in range(1, pivot + 1):
        left_xor ^= i
    for i in range(pivot + 1, n + 1):
        right_xor ^= i

    for ele in arr:
        if ele <= pivot:
            left_xor ^= ele
        else:
            right_xor ^= ele
    return left_xor, right_xor

if __name__ == "__main__":
    data = [x for x in range(1, 1000)]
    data.remove(43)
    data.remove(12)

    print missing_two(data)
