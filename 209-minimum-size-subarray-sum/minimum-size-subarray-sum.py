class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target==0:
            return 0
        l=0
        mn=float('inf')
        cur_sm=0
        for r in range(len(nums)):
            cur_sm+=nums[r]
            while cur_sm>=target:
                mn=min(mn,r-l+1)
                cur_sm-=nums[l]
                l+=1
        return mn if mn!=float('inf') else 0
        