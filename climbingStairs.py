"""
https://leetcode.com/problems/climbing-stairs/
@date: 2021-08-25
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        a, b = 1, 2
        for i in range(0, n - 2):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(5))
