from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(candidates, begin, size, path, res, target):
            if target == 0:
                res.append(path)
                return
            if target < 0:
                return
            
            for i in range(begin, size):
                dfs(candidates, i, size, path + [candidates[i]], res, target - candidates[i])

        size = len(candidates)
        if size == 0:
            return []
        path = []
        res = []
        dfs(candidates, 0, size, path, res, target)
        return res


if __name__ == '__main__':
    # 深度优先遍历+回溯
    # ======= Test Case =======
    candidates = [2,3,6,7]
    target = 7
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.combinationSum(candidates, target)
    print(res)