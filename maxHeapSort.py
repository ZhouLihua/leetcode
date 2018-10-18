#! /usr/bin/env python


"""
heap sort is an in-place algorithm
heap sort is not stable typically
Time complexity: log(n)*n   O(nlogn)
"""

def heapify(arr, n, index):
    parent = index
    left = 2 * parent + 1
    right = 2 * parent + 2

    if left < n and arr[left] > arr[parent]:
        parent = left
    
    if right < n and arr[right] > arr[parent]:
        parent = right
    
    if parent != index:
        arr[parent], arr[index] = arr[index], arr[parent]
        heapify(arr, n, parent)


def heapsort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    heapsort(arr)
    for i in arr:
        print i
