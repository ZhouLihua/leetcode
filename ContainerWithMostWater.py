class Solution(object):
    def maxArea_1(self, height):
        """
        :type height: List[int]
        :rtype: int
        O(N^2)
        """
        max_area = 0
        for i in range(0, len(height)):
            for j in range(i, len(height)):
                area = min(height[i], height[j]) * (j - i)
                if area > max_area:
                    max_area = area
        return max_area

    def maxArea(self, height):
        """
        :param height:
        :return:
        O(N) 
        """
        low = 0
        high = len(height) - 1
        max_area = 0
        while low < high:
            area = min(height[low], height[high]) * (high - low)
            if area > max_area:
                max_area = area
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area

if __name__ == "__main__":
    solution = Solution()
    assert solution.maxArea_1([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49