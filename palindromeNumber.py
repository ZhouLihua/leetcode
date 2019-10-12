class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        new = 0
        old = x
        while x:
            new *= 10
            new += x % 10
            x /= 10
        return new == old


if __name__ == "__main__":
    solution = Solution()
    print solution.isPalindrome(121)
    print solution.isPalindrome(-121)