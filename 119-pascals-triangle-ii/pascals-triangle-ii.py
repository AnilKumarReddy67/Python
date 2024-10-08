class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        return self.res(rowIndex)
    def res(self,idx)->List[int]:
        if idx==0:
            return [1]
        prev=self.res(idx-1)
        new=[1]*(idx+1)
        for i in range(1,idx):
            new[i]=prev[i-1]+prev[i]
        return new

