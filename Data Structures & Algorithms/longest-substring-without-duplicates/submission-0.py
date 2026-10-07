class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        t = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in t:
                t.remove(s[l])
                l+=1
            t.add(s[r])
            res = max(res, (r-l + 1))
        return res
