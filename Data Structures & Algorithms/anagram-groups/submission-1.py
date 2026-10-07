class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}
        for s in strs:
            sorteds = ''.join(sorted(s))
            if sorteds not in ana:
                ana[sorteds] = [s]
            else:
                ana[sorteds].append(s)
        return ana.values()