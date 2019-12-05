class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last = len(nums)
        if last == 1:
            return 1
        lindex, rindex = 0, 1
        while rindex < len(nums):
            if nums[rindex] == nums[lindex]:
                rindex += 1
            else:
                lindex += 1
                nums[lindex] = nums[rindex]
                rindex += 1
        return lindex + 1


if __name__  == "__main__":
    solution = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert solution.removeDuplicates(nums) == 5
    print nums[0:5]