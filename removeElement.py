class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        index = 0
        next_start = None
        end = len(nums)
        while index < end:
            if nums[index] == val:
                if not next_start:
                    next_start = index + 1
                while next_start < end and nums[next_start] == val:
                    next_start += 1
                if next_start == end:
                    break
                nums[index], nums[next_start] = nums[next_start], nums[index]
                index += 1
                next_start += 1
            else:
                index += 1

        return index


if __name__ == "__main__":
    solution = Solution()
    nums = [0,1,2,2,3,0,4,2]
    assert solution.removeElement(nums, 2) == 5
    print nums
