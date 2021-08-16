class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key = lambda x: x[0])
        stack = [intervals[0]]
        for interval in intervals:
            top = stack.pop()
            if top[1] < interval[0]:
                stack.append(top)
                stack.append(interval)
            else:
                stack.append([top[0], max(top[1], interval[1])])
        return stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
