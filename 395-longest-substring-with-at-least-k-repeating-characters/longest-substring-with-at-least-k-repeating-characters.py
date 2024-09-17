class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        mp={}
        for char in s:
            mp[char]=mp.get(char,0)+1
        for char in mp:
            if mp[char]<k:
                return max(self.longestSubstring(sub,k) for sub in s.split(char))
        return len(s)
        