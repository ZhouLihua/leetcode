"""
https://leetcode.com/problems/unique-paths/
"""

class Solution:
    def uniquePaths(self, m, n):
        matrix = [[0] * n for _ in range(m)]

        # matrix[0][0] = 1
        for i in range(m):
            matrix[i][0] = 1

        for j in range(n):
            matrix[0][j] = 1

        for k in range(1, m):
            for p in range(1, n):
                matrix[k][p] = matrix[k - 1][p] + matrix[k][p - 1]

        return matrix[-1][-1]

    def uniquePathsI(self, m, n):
        if m == 1 or n == 1:
            return 1
        else:
            result = self.uniquePathsI(m - 1, n) + self.uniquePathsI(m, n - 1)
            print m, n, result
            return result


if __name__ == "__main__":
    solution = Solution()

    # assert solution.uniquePaths(3, 7) == 28
    print solution.uniquePathsI(3, 7)
