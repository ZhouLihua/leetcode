class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        window = set()
        left = 0
        max_len, cur_len = 0, 0
        for i in range(0, len(s)):
            cur_len += 1
            while s[i] in window:
                window.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            window.add(s[i])
        return max_len


if __name__ == "__main__":
    solution = Solution()
    assert 3 == solution.lengthOfLongestSubstring("pwwkew")
    assert 3 == solution.lengthOfLongestSubstring("abcabcbb")
    assert 1 == solution.lengthOfLongestSubstring(" ")
    assert 2 == solution.lengthOfLongestSubstring("aab")
    assert 3 == solution.lengthOfLongestSubstring("dvdf")