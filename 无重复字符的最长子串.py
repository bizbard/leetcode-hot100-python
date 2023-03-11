class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        cur_length = 1
        max_length = 0
        left = 0
        lookup = set()
        lookup.add(s[0])

        for i in range(1, len(s)):
            cur_length += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_length -= 1

            lookup.add(s[i])
            max_length = max(cur_length, max_length)

        return max_length


if __name__ == '__main__':
    # ======= Test Case =======
    s = "pwwkew"
    # ====== Driver Code ======
    Sol = Solution()
    res = Sol.lengthOfLongestSubstring(s)
    print(res)