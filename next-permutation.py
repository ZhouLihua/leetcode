"""
https://leetcode.com/problems/next-permutation/
"""


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        if length < 2:
            return nums
        i = length - 2
        # first finding the first continue decending index
        while i >= 0 and nums[i] >= nums[i + 1]:
                i -= 1
        if i >= 0:
            j = length - 1
            # find the num just bigger then the descending number, then swap them
            while j > i and nums[j] <= nums[i]:
                    j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # reverse the numbers from index to the end
        nums[i+1:] = nums[i+1:][::-1]
        return nums


if __name__ == "__main__":
    solution = Solution()
    assert solution.nextPermutation([1, 2, 3]) == [1, 3, 2]
    assert solution.nextPermutation([3, 2, 1]) == [1, 2, 3]
    assert solution.nextPermutation([1, 1, 5]) == [1, 5, 1]
    assert solution.nextPermutation([1, 3, 2]) == [2, 1, 3]
