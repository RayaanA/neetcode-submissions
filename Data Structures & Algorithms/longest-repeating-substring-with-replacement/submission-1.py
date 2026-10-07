class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        l = 0
        maxf = 0
        for r in range(len(s)):
            chars[s[r]] = 1+chars.get(s[r],0)
            maxf = max(maxf, chars[s[r]])
            if (k < (r-l+1-maxf)):
                chars[s[l]]-=1
                l+=1
        return r-l+1