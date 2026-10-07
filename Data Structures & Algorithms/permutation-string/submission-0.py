class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check = {}
        for char in s1:
            check[char] = 1+check.get(char,0)
        l=0
        r=len(s1)
        while (r <= len(s2)):
            temp = {}
            for char in s2[l:r]:
                temp[char] = 1+temp.get(char,0)
            if temp == check:
                return True
            l+=1
            r+=1
        return False