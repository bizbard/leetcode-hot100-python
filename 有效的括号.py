class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {
            '(': ')',
            '[': ']',
            '{': '}',
            '?': '?',
        }

        stak = ['?']
        for i in range(len(s)):
            if s[i] in lookup:
                stak.append(s[i])
            else:
                chartop = stak.pop()
                if lookup[chartop] != s[i]:
                    return False
        return True if stak.pop() == '?' else False


if __name__ == '__main__':
    # 辅助栈，注意边界，当栈为空时，.pop()报错
    # ======= Test Case =======
    s = "()[]{}"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.isValid(s)
    print(res)