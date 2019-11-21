class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_len = len(nums)
        i = 0
        results = []
        while i < nums_len - 3:
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                while j < nums_len - 2:
                    if j == i + 1 or nums[j] != nums[j - 1]:
                        low = j + 1
                        high = nums_len - 1
                        while low < high:
                            if nums[i] + nums[j] + nums[low] + nums[high] == target:
                                results.append([nums[i], nums[j], nums[low], nums[high]])
                                while low + 1 < high and nums[low + 1] == nums[low]:
                                    low += 1
                                while high - 1> low and nums[high - 1] == nums[high]:
                                    high -= 1
                                low += 1
                                high -= 1
                                continue
                            if nums[i] + nums[j] + nums[low] + nums[high] < target:
                                while low + 1 < high and nums[low + 1] == nums[low]:
                                    low += 1
                                low += 1
                                continue
                            if nums[i] + nums[j] + nums[low] + nums[high] > target:
                                while high - 1 > low and nums[high - 1] == nums[high]:
                                    high -= 1
                                high -= 1
                                continue
                    j += 1
            i += 1
        return results


if __name__ == "__main__":
    solution = Solution()
    assert solution.fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1]
    ]

    assert solution.fourSum([0, 0, 0, 0], 0) == [
        [0, 0, 0, 0]
    ]