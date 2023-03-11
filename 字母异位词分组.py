from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resdic = {}
        for i in range(len(strs)):
            if ''.join(sorted(list(strs[i]))) in resdic:
                key = ''.join(sorted(list(strs[i])))
                resdic[key].append(strs[i])
            else:
                key = ''.join(sorted(list(strs[i])))
                resdic[key] = [strs[i]]
        return list(resdic.values())

if __name__ == '__main__':
    # 利用字典序
    # ======= Test Case =======
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.groupAnagrams(strs)
    print(res)