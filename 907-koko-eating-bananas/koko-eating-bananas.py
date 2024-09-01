class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def minEat(speed):
            c=0
            for pile in piles:
                c+=(pile+speed-1)//(speed)
            return c<=h
        
        l=1
        r=max(piles)
        while l<r:
            m=(l+r)//2
            if minEat(m):
                r=m
            else:
                l=m+1
        return l
