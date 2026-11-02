class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans=""
        if len(strs)>0:
            a=sorted(strs)
            smallest=a[0]
            largest=a[-1]
            i=0
            # for i in range(len(smallest)-1):
            while((i<len(smallest)) and (smallest[i]==largest[i]) ):
                ans+=smallest[i]
                i+=1
        return ans