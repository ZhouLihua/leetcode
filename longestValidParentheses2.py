"""
https://leetcode.com/problems/longest-valid-parentheses/
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        max_len = 0
        stack.append(-1)
        for i in range(0, len(s)):
            if s[i] == ")":
                if stack:
                    stack.pop()
                    if stack:
                        max_len = max(max_len, i - stack[-1])
                    else:
                        stack.append(i)
            else:
                stack.append(i)
        return max_len


if __name__ == "__main__":
    solution = Solution()
    assert solution.longestValidParentheses("(()") == 2
    assert solution.longestValidParentheses(")()())") == 4
    assert solution.longestValidParentheses("") == 0
    assert solution.longestValidParentheses("()") == 2
    assert solution.longestValidParentheses("(()))())(") == 4
