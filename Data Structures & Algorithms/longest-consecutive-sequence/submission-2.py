class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        res = sorted(set(nums))
        length = 1
        past = 10000000000
        maxLength = 0
        print(res)
        for x in res:
            print(length)
            if past+1 == x:
                past += 1
                length += 1
            else:
                past = x
                maxLength = max(maxLength,length)
                length = 1
        return max(maxLength,length)