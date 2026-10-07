class Solution:
    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        for i in range (len(nums)):
            for j in range (len(nums)-1, i, -1):
                if nums[i]+nums[j] == target:
                    return [i,j]"""
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(nums):
            need = target-num
            if need in seen:
                return [seen[need],i]
            seen[num] = i
