# 题目过难，略过
from typing import List

class node:
    def __init__(self,value,step=0):
        self.value = value
        self.step = step
    def __str__(self):
        return '<value:{}, step:{}>'.format(self.value,self.step)

class Solution:
    def numSquares(self, n: int) -> int:
        queue = [node(n)]
        visited = set([node(n).value])
        
        while queue:
            vertex = queue.pop(0)
            residuals = [vertex.value - n*n for n in range(1,int(vertex.value**.5)+1)]
            for i in residuals:
                new_vertex = node(i, vertex.step+1)
                if i==0:                   
                    return new_vertex.step
                    
                elif i not in visited:
                    queue.append(new_vertex)
                    visited.add(i)
                                        
        return -1
            

if __name__ == '__main__':
    # ======= Test Case =======
    n = 12
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.numSquares(n)
    print(res)