class Solution:
    def generateMatrix(self, n):
        result = [[-1] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        item = 1
        while left <= right and top <= bottom:
            # left to right
            for i in range(left, right + 1):
                result[top][i] = item
                item += 1

            for j in range(top + 1, bottom + 1):
                result[j][right] = item
                item += 1

            for m in range(right - 1, left - 1, -1):
                result[bottom][m] = item
                item += 1

            for n in range(bottom - 1, top, -1):
                result[n][left] = item
                item += 1

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateMatrix(4))
