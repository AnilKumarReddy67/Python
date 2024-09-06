class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return [[1]]
        else:
            return self.getAllRows(numRows-1)
    
    def getAllRows(self,num):
        if num==0:
            return [[1]]
        prec=self.getAllRows(num-1)
        ln=len(prec[-1])
        prec.append([1])
        for i in range(0,ln-1):
            prec[-1].append(prec[-2][i]+prec[-2][i+1])
        prec[-1].append(1)
        return prec