class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        # change the s to odd length
        s1 = "*"
        for c in s:
            s1 += c
            s1 += "*"

        index = 1
        strLength = len(s1)
        radius = [1]
        while index < strLength:
            j = 0
            k = 0
            while True:
                if index - j < 0 or index + j > strLength - 1:
                    break
                if s1[index - j] == s1[index + j]:
                    k += 1
                    j += 1
                else:
                    break
            radius.append(k)
            index += 1
        maxIndex = 0
        maxRadius = 1
        for k, v in enumerate(radius):
            if v > maxRadius:
                maxIndex, maxRadius = k, v
        # maxRadius - 1 for itself is one
        return s1[maxIndex - (maxRadius - 1) + 1: maxIndex + (maxRadius - 1) + 1: 2]



if __name__ == "__main__":
    solution = Solution()
    print solution.longestPalindrome("abcbcde")
    print solution.longestPalindrome("abba")
    print solution.longestPalindrome("cbbd")
    print solution.longestPalindrome("ac")