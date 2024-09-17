class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        rep=set()
        seen=set()
        if len(s)<10:
            return []
        for i in range(len(s)):
            ss=s[i:i+10]
            if ss in seen:
                rep.add(ss)
            else:
                seen.add(ss)
        return list(rep)
