class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def comb(idx,l,sm):
            if len(l)==k:
                if sm==n:
                    res.append(l)
                return
            for i in range(idx,10):
                cur=sm+i
                if cur<=n:
                    comb(i+1,l+[i],cur)
        comb(1,[],0)
        return res
