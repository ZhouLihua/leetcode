#! /usr/bin/env python

"""
Given an array, write a function to find any subarray that sums to zero,
if one exists
eg.
zero_sum([1, 2, -5, 1, 2, -1]) = [1, 2, -5, 1, 2, -1] or [2, -5, 1, 2]
"""

def zero_sum(arr):
    sum = []
    sum.append(0)
    for i in range(0, len(arr)):
        sum.append(sum[-1] + arr[i])
    map = dict()
    import pdb
    pdb.set_trace()
    for i in range(0, len(sum)):
        old_index = map.get(sum[i])
        if old_index == None:
            map[sum[i]] = i
        else:
            return arr[old_index: i]
    return None


if __name__ == "__main__":
    data = [1, -5, 1, 2, -1, 2]
    print zero_sum(data)
