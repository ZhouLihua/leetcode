#! /usr/bin/env python

"""
Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
"""

def longest_incremental_substr(arr):
    temp = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                temp[i] = max(temp[i], temp[j] + 1)
    
    print temp
    return max(temp)

if __name__ == "__main__":
    arr = [1, 3, 2, 2, 7, 6, 9, 11]
    print(longest_incremental_substr(arr))
