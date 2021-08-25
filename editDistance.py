"""
https://leetcode.com/problems/edit-distance/
@Date: 2021-08-25
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:
            return len(word2)

        if not word2:
            return len(word1)

        if not word1 and not word2:
            return 0

        m, n = len(word1), len(word2)

        matrix = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, m + 1):
            matrix[0][j] = j

        for k in range(1, n + 1):
            matrix[k][0] = k

        for p in range(1, m + 1):
            for q in range(1, n + 1):
                if word1[p - 1] == word2[q - 1]:
                    matrix[q][p] = matrix[q - 1][p - 1]
                else:
                    matrix[q][p] = 1 + min(matrix[q - 1][p - 1], matrix[q - 1][p], matrix[q][p - 1])

        return matrix[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance("horse", "ros"))
