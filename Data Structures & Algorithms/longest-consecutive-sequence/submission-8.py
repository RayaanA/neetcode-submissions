class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = sorted(set(nums))
        #print (numSet)
        maxCnt = 0

        cnt = 1

        prev = -math.inf
        for num in numSet:
            #print(f"num:{num}, prev:{prev}, cnt:{cnt},maxCnt:{maxCnt}")
            if num-1==prev:
                cnt+=1
                prev = num
            else:
                maxCnt=max(maxCnt,cnt)
                cnt=1
                prev = num
        maxCnt = max(maxCnt, cnt)
        return maxCnt