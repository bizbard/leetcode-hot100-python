from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        res = []
        res.append([None])
        res.append(['()'])
        
        for i in range(2, n + 1):
            mid = []
            for j in range(i):
                l1 = res[j]
                l2 = res[i - j - 1]
                for k1 in l1:
                    for k2 in l2:
                        if k1 == None:
                            k1 = ''
                        if k2 == None:
                            k2 = ''
                        mid.append('('+k1+')'+k2)
            res.append(mid)

        return res[n]
        

if __name__ == '__main__':
    # ======= Test Case =======
    n = 3
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.generateParenthesis(n)
    print(res)