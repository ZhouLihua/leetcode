#!/usr/bin/env python


def sum_count(arr, index, total):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if index < 0:
        return 0

    if arr[index] > total:
        return sum_count(arr, index - 1, total)

    return sum_count(arr, index - 1, total) + sum_count(arr, index - 1, total - arr[index])


def helper(arr, total):
    return sum_count(arr, len(arr) - 1, total)


def sum_count_dp(arr, index, total, memo):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if index < 0:
        return 0

    key = "-".join([str(total), str(index)])
    if key in memo.keys():
        return memo[key]

    if arr[index] > total:
        sum = sum_count_dp(arr, index-1, total, memo)
        memo[key] = sum
        return sum
    sum = sum_count_dp(arr, index-1, total, memo) + sum_count_dp(arr, index-1, total - arr[index], memo)
    memo[key] = sum
    return sum


def helper_dp(arr, total):
    memo = dict()
    return sum_count_dp(arr, len(arr) - 1, total, memo)


if __name__ == "__main__":
    arr_test = [1, 2, 3, 4, 5]
    print(helper(arr_test, 10))
    print(helper_dp(arr_test, 10))
