"""
https://leetcode.com/problems/trapping-rain-water/
time complex O(n)
space complex O(n)
"""

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        width = len(height)
        water = 0
        stack = []
        count = 0
        for i in range(width):
            if i == 0 or height[i] < height[i-1]:
                stack.append(i)
                count = count + 1
            else:
                # loop to find all stack.top() height < height[i]
                while count and height[stack[-1]] < height[i]:
                    if count < 2:
                        # stack.append(i)
                        break
                    top1 = stack.pop()
                    top2 = stack.pop()
                    count = count - 2
                    if height[top2] > height[top1]:
                        _water = (min(height[i], height[top2]) - height[top1]) * (i - top2 - 1)
                        water = water + _water
                        stack.append(top2)
                        count += 1
                    else:
                        stack.append(top1)
                        count = count + 1
                stack.append(i)
                count = count + 1
        return water


if __name__ == "__main__":
    solution = Solution()
    # print solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
    assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert solution.trap([2,1,0,2]) == 3