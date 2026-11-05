class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len=min(len(word1),len(word2))
        ans=""
        res=0
        for i in range(min_len):
            ans+=word1[i]
            ans+=word2[i]
            res=i
        res+=1
        print(res)
        if len(word1)-res>0:
            ans+=word1[res:]
        elif len(word2)-res>0:
            ans+=word2[res:]
        return ans




        