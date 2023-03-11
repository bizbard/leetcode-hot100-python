from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res = []
        lookup = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

        def dialNumber(conbination, nextdigits):
            if nextdigits == '':
                res.append(conbination)
            else:
                for digit in lookup[nextdigits[0]]:
                    dialNumber(conbination+digit, nextdigits[1:])
        
        dialNumber('', digits)
        return res


if __name__ == '__main__':
    # 回溯，有点像树的层序遍历
    # ======= Test Case =======
    digits = "23"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.letterCombinations(digits)
    print(res)
