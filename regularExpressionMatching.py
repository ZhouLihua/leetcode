class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        T = [[True] + [False]*len(p)] + [[False]*(len(p)+1) for _ in range(len(s))]
        s, p = ' ' + s, ' ' + p
        for i in range(len(T)):
            for j in range(1, len(T[0])):
                if p[j] == '*':
                    if i == 0 or T[i][j-2]:  # zero of the character before *
                        T[i][j] = T[i][j-2]
                    elif i > 0 and (s[i] == p[j-1] or p[j-1] == '.'):  # one or more of the characters before *
                        T[i][j] = T[i-1][j]
                elif i > 0 and (s[i] == p[j] or p[j] == '.'):  # exact match at i and j or a '.'
                    T[i][j] = T[i-1][j-1]
        return T[-1][-1]


if __name__ == "__main__":
    solution = Solution()
    print solution.isMatch("aa", "a")
    print solution.isMatch("aa", "a*")
    print solution.isMatch("ab", ".*")
    print solution.isMatch("aab", "c*a*b")
    print solution.isMatch("mississippi", "mis*is*p*.")
    print solution.isMatch("ab", ".*c")

