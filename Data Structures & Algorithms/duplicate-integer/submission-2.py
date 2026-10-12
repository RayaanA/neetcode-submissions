class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numset = set(nums)
        return False if len(nums) == len(numset) else True