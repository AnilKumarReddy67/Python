from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=collections.defaultdict(set)
        cols=collections.defaultdict(set)
        boxes=collections.defaultdict(set)
        for i in range(9):
            for j in range(9):
                # process only it is a numbers
                val=board[i][j]
                if val!='.':
                    if val in rows[i] or val in cols[j] or val in boxes[(i//3,j//3)]:
                        return False
                    #populate the values
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i//3,j//3)].add(val)
        return True
