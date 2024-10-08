class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp={}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[nums[i]]=1
            else:
                mp[nums[i]]+=1
        for k,v in mp.items():
            if v>=2:
                return True
        return False