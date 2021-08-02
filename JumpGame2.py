"""
https://leetcode.com/problems/jump-game-ii/
"""


class Solution:
    def __init__(self):
        pass

    def jump(self, nums):
        end = len(nums)
        if end < 2:
            return 0

        left, right = 0, nums[0]
        farthest = 0
        jumps = 1
        while right < end - 1:
            jumps = jumps + 1
            # greedy, find the max len in the range of before max len
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
        return jumps


if __name__ == "__main__":
    solution = Solution()
    print(solution.jump([2, 3, 0, 1, 4]))
