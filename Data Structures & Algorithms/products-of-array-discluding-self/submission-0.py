class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        og = [1,2,4,6]
        =[1,1,1,1] pre = 1
        =[1,1,1,1] pre = 2
        [1,1,2,1] pre = 8
        [1,1,2,8]

        [1,1,2,8] post = 1

        """
        length = len(nums)
        res = [1]*(length)
        pre = 1
        for i in range(length):
            res[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(length-1,-1,-1):
            res[i] *= post
            post *= nums[i]
        return res