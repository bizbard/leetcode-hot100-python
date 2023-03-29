import collections
from typing import List, Optional
    

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        res = []
        people.sort(key=lambda x: (-x[0], x[1]))
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            else:
                res.insert(p[1], p)
                
        return res

if __name__ == '__main__':
    # ======= Test Case =======
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.reconstructQueue(people)
    print(res)