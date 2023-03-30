import collections
from typing import List, Optional
    
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        res = [0] * len(temperatures)
        for i in range(len(temperatures)):

            while stack and stack[-1][1] < temperatures[i]:
                item = stack.pop()
                index = item[0]
                res[index] = i - index

            stack.append((i, temperatures[i]))
        return res 


if __name__ == '__main__':
    # ======= Test Case =======
    temperatures = [73,74,75,71,69,72,76,73]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.dailyTemperatures(temperatures)
    print(res)