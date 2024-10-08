from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mp=defaultdict(list)
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]]=1
            else:
                mp[nums[i]]+=1
        n=len(nums)//2
        for k,v in mp.items():
            if v>n:
                return k
