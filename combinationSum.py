"""
https://leetcode.com/problems/combination-sum/
"""
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def dfs(path, target, previous):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in candidates:
                if i >= previous:
                    dfs(path + [i], target - i, i)
        dfs([], target, -1)
        return result


if __name__ == "__main__":
    solution = Solution()
    assert solution.combinationSum([2,3,6,7], 7) == [
        [2, 2, 3],
        [7]
    ]
    assert solution.combinationSum([2,3,5], 8) == [
        [2,2,2,2],
        [2,3,3],
        [3,5]
    ]