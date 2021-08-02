class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        # step 1, 根据(x,y)对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # step 2, 根据x轴对称旋转
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]

        return matrix


if __name__ == "__main__":
    solution = Solution()
    m = [[1,2,3],[4,5,6],[7,8,9]]
    print(solution.rotate(m))