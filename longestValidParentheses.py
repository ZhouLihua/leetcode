"""
https://leetcode.com/problems/longest-valid-parentheses/
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0 for _ in s]
        for i in range(1, len(s)):
            if s[i] == ")":
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2 if i > 1 else 2
                else:
                    if i - dp[i-1] > 0 and s[i - dp[i - 1] - 1] == "(":
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] -2] if i > 1 else dp[i-1] + 2
        return max(dp)

if __name__ == "__main__":
    solution = Solution()
    assert solution.longestValidParentheses("(()") == 2
    assert solution.longestValidParentheses(")()())") == 4
    assert solution.longestValidParentheses("") == 0
    assert solution.longestValidParentheses("()") == 2
    assert solution.longestValidParentheses("(()))())(") == 4
