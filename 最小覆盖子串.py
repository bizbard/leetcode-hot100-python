# 题目过难，略过

import collections

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        needDic = collections.defaultdict(int)
        for c in t:
            needDic[c]+=1
        needCnt = len(t)
        print(needDic)

        i = 0
        res=(0,float('inf'))
        for j, item in enumerate(s):
            if needDic[item] > 0:
                needCnt -= 1
            needDic[item] -= 1
            if needCnt == 0:
                while True:
                    c=s[i] 
                    if needDic[c]==0:
                        break
                    needDic[c]+=1
                    i += 1
                if j-i<res[1]-res[0]:
                    res=(i,j)
                needDic[s[i]] += 1
                needCnt += 1
                i+=1
        return '' if res[1]>len(s) else s[res[0]:res[1]+1]
            

if __name__ == '__main__':
    # ======= Test Case =======
    s = "ADOBECODEBANC"
    t = "ABC"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.minWindow(s, t)
    print(res)