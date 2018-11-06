#! /usr/bin/env python

"""
Given a set of non-negative integers, and a value sum,
determine if there is a subset of the given set with sum equal to given sum.

The isSubsetSum problem can be divided into two subproblems
    a) Include the last element, recur for n = n-1, sum = sum – set[n-1]
    b) Exclude the last element, recur for n = n-1.
If any of the above the above subproblems return true, then return true.
"""


def is_subset_exist(subset, index, sum):
    if sum == 0:
        return True
    if index == 0 and sum != 0:
        return False

    return is_subset_exist(subset, index - 1, sum) or \
           is_subset_exist(subset, index - 1, sum - subset[index - 1])


def is_subset_exist_dp(subset, index, sum, memo):
    key = "-".join([str(sum), str(index)])
    if key in memo.keys():
        return memo.get(key)

    if sum == 0:
        return True
    if index == 0 and sum != 0:
        return False
    val = is_subset_exist_dp(subset, index-1, sum, memo) or \
          is_subset_exist_dp(subset, index-1, sum - sub_set[index-1], memo)
    memo[key] = val
    return val


def helper(arr, sum):
    memo = dict()
    return is_subset_exist_dp(arr, len(arr), sum, memo)


if __name__ == "__main__":
    sub_set = [3, 34, 4, 12, 5, 2, 1, 23, 99, 32, 78, 8]
    print(is_subset_exist(sub_set, len(sub_set), 100))
    print(helper(sub_set, 100))
