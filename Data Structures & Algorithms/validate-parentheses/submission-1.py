class Solution:
    def isValid(self, s: str) -> bool:
        Map =   {
                ")" : "(",
                "}" : "{",
                "]" : "["
                }
        res = []
        for char in s:
            if char not in Map:
                res.append(char)
                continue
            if not res or Map[char] !=res[-1]:
                return False
            res.pop()
        return not res
    