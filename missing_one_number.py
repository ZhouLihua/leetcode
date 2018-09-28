#!/usr/bin/env python


"""
Given a sequence [1, 2, ..., N], there is one element missed,
find the missed number
"""


def missing_num(arr, last):
    total_XOR = 0
    arr_XOR =  0
    for i in range(1, last + 1):
        total_XOR ^= i
    for j in arr:
        arr_XOR ^= j
    
    return total_XOR ^ arr_XOR


if __name__ == "__main__":
    test_arr = [1, 2, 3, 5, 6, 7]
    print missing_num(test_arr, 7)

    test_arr_1 = [x for x in range(1, 10001)]
    test_arr_1.remove(4999)

    print missing_num(test_arr_1, 10000)
