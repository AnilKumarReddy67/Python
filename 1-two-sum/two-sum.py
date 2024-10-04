class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}
        for i,num in enumerate(nums):
            res=target-num
            if res in mp:
                return [mp[res],i]
            mp[num]=i
        