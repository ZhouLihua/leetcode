"""
https://leetcode.com/problems/search-insert-position/
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    solution = Solution()
    assert solution.searchInsert([1,3,5,6], 5) == 2
    assert solution.searchInsert([1,3,5,6], 2) == 1
    assert solution.searchInsert([1,3,5,6], 7) == 4
    assert solution.searchInsert([1,3,5,6], 0) == 0