class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)+1
        res = [[] for _ in range(size)]

        resdic = {}
        for num in nums:
            resdic[num] = 1 + resdic.get(num,0)
        for n, c in resdic.items():
            res[c].append(n)
        print(res)

        result = []
        for i in range(size-1,0,-1):
            for num in res[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result