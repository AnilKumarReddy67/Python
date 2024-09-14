from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_ln=len(words[0])
        word_count=len(words)
        total_ln=word_ln*word_count
        word_freq=Counter(words)

        res=[]
        for i in range(word_ln):
            left=i
            cur_freq={}
            c=0

            for right in range(i,len(s)-word_ln+1,word_ln):
                word=s[right:right+word_ln]

                if word in word_freq:
                    cur_freq[word]=cur_freq.get(word,0)+1
                    c+=1

                    while cur_freq[word]>word_freq[word]:
                        left_word=s[left:left+word_ln]
                        cur_freq[left_word]-=1
                        c-=1
                        left+=word_ln
                    if c==word_count:
                        res.append(left)
                else:
                    cur_freq.clear()
                    c=0
                    left=right+word_ln
        return res
