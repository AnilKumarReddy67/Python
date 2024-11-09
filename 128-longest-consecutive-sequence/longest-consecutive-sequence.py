class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        ln=0
        for st in nums:
            if st-1 not in nums_set:
                end=st+1
                while end in nums_set:
                    end+=1
                ln=max(ln,end-st)
        return ln