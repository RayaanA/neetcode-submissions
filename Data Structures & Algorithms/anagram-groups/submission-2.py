class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keyvals = {}
        for word in strs:
            setw = str(sorted(word))
            if keyvals.get(setw) != None:
                keyvals[setw].append(word)
            else:
                keyvals[setw] = [word]
        return list(keyvals.values())

