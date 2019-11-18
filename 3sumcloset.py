import sys

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len < 3:
            return 0
        nums.sort()
        result = sys.maxint
        diff = sys.maxint
        start = 0
        while start < nums_len - 2:
            i = start + 1
            j = nums_len - 1
            while i < j:
                total = nums[start] + nums[i] + nums[j]
                if total == target:
                    return target
                if total < target:
                    i += 1
                if total > target:
                    j -= 1
                _diff = abs(total - target)
                if _diff < diff:
                    diff = _diff
                    result = total
            start += 1
        return result



if __name__ == "__main__":
    solution = Solution()
    assert solution.threeSumClosest([-1, 2, 1, -4], 1) == 2