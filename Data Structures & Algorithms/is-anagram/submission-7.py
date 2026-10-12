class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        for char in s:
            if char in dicts:
                dicts[char] +=1
            else:
                dicts[char]=1
        for char in t:
            if char in dictt:
                dictt[char]+=1
            else:
                dictt[char]=1
        return dictt==dicts