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

"""
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            groups[tuple(count)].append(s)

        return list(groups.values())"""