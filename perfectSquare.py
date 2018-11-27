#!/usr/bin/env python

"""
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n. For example, given n = 12 ,
return 3 because 12 = 4 + 4 + 4 ; given n = 13 , return 2 because 13
= 4 + 9
"""
import sys


def find_perfect_squares(n):
    arr = [sys.maxint for _ in range(0, n+1)]
    arr[0] = 0
    for i in range(0, n+1):
        j = 1
        while i + j*j <= n:
            arr[i + j*j] = min(arr[i + j*j], arr[i] + 1)
            j = j + 1
    print(arr)
    return arr[n]


def min(a, b):
    return a if a <= b else b


if __name__ == "__main__":

    print(find_perfect_squares(16))
