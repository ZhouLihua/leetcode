"""
https://leetcode.com/problems/maximum-subarray/
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        sum = nums[0]
        current_max = nums[0]
        for index in range(1, len(nums)):
            current_max = max(current_max + nums[index], nums[index])
            sum = max(current_max, sum)
        return sum


if __name__ == "__main__":
    solution = Solution()
    assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6


