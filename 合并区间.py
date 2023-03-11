from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []

        intervals.sort(key = lambda x: x[0])
        prev = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= prev[1]:
                res.append([prev[0], intervals[i][1]])
                prev = [prev[0], intervals[i][1]]
            else:
                res.append(intervals[i])
                prev = intervals[i]

        return res
            

if __name__ == '__main__':
    # ======= Test Case =======
    intervals = [[1,4],[4,5]]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.merge(intervals)
    print(res)