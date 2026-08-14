class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        t=0
        for i in range (len(nums)):
            if i%2==0:
                t+=nums[i]
            elif i%2==1:
                t-=nums[i]
        return t