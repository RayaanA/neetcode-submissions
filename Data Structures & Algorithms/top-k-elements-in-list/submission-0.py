class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            dic[num] = 1+dic.get(num,0)
        lis = [[] for i in range(len(nums) + 1)]
        for num,count in dic.items():
            lis[count].append(num)
        res = []
        for n in range(len(lis)-1,-1,-1):
            for c in lis[n]:
                res.append(c)
                if (len(res) == k):
                    return res