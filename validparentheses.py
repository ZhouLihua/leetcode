class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pairs = dict()
        pairs[")"] = "("
        pairs["]"] = "["
        pairs["}"] = "{"
        stack = []
        lefts = ["(", "[", "{"]
        for c in s:
            if c in lefts:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if pairs.get(c) == left:
                    continue
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    solution = Solution()
    assert solution.isValid("()") == True
    assert solution.isValid("()[]{}") == True
    assert solution.isValid("(]") == False
    assert solution.isValid("([)]") == False
    assert solution.isValid( "{[]}") == True
    assert solution.isValid("}") == False
    