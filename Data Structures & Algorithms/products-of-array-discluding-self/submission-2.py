class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pre = [1]*l
        post = [1]*l
        res = [1]*l
        for i in range(1,l):
            pre[i] = pre[i-1]*nums[i-1]

        for i in range(l-2,-1,-1):
            post[i] = post[i+1]*nums[i+1]
        print (pre)
        print(post)
        for i in range (0,l):
            res[i] = pre[i]*post[i]
        return res