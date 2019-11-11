class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        result = []
        arr_length = len(nums)
        nums.sort()
        index = 0
        while index < arr_length - 2 and nums[index] <= 0:
            if index == 0 or nums[index] != nums[index - 1]:
                low = index + 1
                high = arr_length - 1
                while low < high:
                    if nums[low] + nums[high] + nums[index] == 0:
                        # there may be more than one case satisfy the requirement
                        result.append([nums[index], nums[low], nums[high]])
                        low += 1
                        high -= 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        while high > low and nums[high] == nums[high + 1]:
                            high -= 1
                    elif nums[low] + nums[high] + nums[index] < 0:
                        low += 1
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                    else:
                        high -= 1
                        while high > low and nums[high] == nums[high + 1]:
                            high -= 1
                index += 1
            else:
                index += 1
        return result


if __name__ == "__main__":
    solution = Solution()
    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    assert result == [[-1, -1, 2], [-1, 0, 1]]
    assert solution.threeSum([0, 0, 0, 0]) == [[0,0,0]]
    assert solution.threeSum([1,-1,-1,0]) == [[-1,0,1]]