"""
https://leetcode.com/problems/first-missing-positive/
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set()
        for num in nums:
            if num > 0:
                num_set.add(num)

        i = 1
        while True:
            if i not in num_set:
                return i
            i = i + 1


if __name__ == "__main__":
    solution = Solution()
    assert solution.firstMissingPositive([1,2,0]) == 3
    assert solution.firstMissingPositive([3,4,-1,1]) == 2
    assert solution.firstMissingPositive([7,8,9,11,12]) == 1