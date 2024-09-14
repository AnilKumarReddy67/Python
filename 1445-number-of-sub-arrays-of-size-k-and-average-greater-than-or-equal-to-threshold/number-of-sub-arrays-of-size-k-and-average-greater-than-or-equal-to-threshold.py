class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        c=0
        win=sum(arr[:k])
        if win/k>=threshold:
            c+=1
        for i in range(k,len(arr)):
            win+=arr[i]-arr[i-k]

            if win/k>=threshold:
                c+=1
        return c