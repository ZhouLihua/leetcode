"""
https://leetcode.com/problems/combination-sum-ii/
"""
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        lens = len(candidates)
        result = []

        def dfs(cur, target, index):
            if target == 0:
                result.append(cur)
                return
            if target < 0:
                return
            for i in range(index, lens):
                # move duplicated
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                dfs(cur + [candidates[i]], target - candidates[i], i+1)

        dfs([], target, 0)
        return result


if __name__ == "__main__":
    solution = Solution()
    print solution.combinationSum2([10,1,2,7,6,1,5], 8)
    assert solution.combinationSum2([10,1,2,7,6,1,5], 8) == [
        [1, 1, 6],
        [1, 2, 5],
        [1, 7],
        [2, 6]
    ]
    assert solution.combinationSum2([2,5,2,1,2], 5) == [
        [1,2,2],
        [5]
    ]