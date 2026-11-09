class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sta=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while sta and temperatures[sta[-1]]<temperatures[i]:
                prev_index=sta.pop()
                res[prev_index]=i-prev_index
            sta.append(i)
        return res
                
        