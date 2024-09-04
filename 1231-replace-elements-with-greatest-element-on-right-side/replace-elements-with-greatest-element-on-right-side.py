class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        mx=-1
        for i in range(n-1,-1,-1):
            val=mx
            mx=max(mx,arr[i])
            arr[i]=val
        return arr
        