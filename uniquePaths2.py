"""
https://leetcode.com/problems/unique-paths-ii/
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        matrix = [[0] * n for _ in range(m)]
        matrix[0][0] = 1 - obstacleGrid[0][0]
        print matrix
        for i in range(1, m):
            matrix[i][0] = matrix[i - 1][0] * (1 - obstacleGrid[i][0])

        for j in range(1, n):
            matrix[0][j] = matrix[0][j - 1] * (1 - obstacleGrid[0][j])

        print matrix
        for k in range(1, m):
            for p in range(1, n):
                matrix[k][p] = (matrix[k - 1][p] + matrix[k][p - 1]) * (1 - obstacleGrid[k][p])

        return matrix[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
