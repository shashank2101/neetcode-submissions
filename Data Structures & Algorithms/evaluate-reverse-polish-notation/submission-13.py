class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta=[]
        operations=['+','-','*','/']
        for i in range(len(tokens)):
            if tokens[i]=='+':
                temp1=sta.pop()
                temp2=sta.pop()
                sta.append(temp1+temp2)
                # print(sta)
            elif tokens[i]=='-':
                temp1=sta.pop()
                temp2=sta.pop()
                sta.append(temp2-temp1)
                # print(sta)
            elif tokens[i]=='*':
                temp1=sta.pop()
                temp2=sta.pop()
                sta.append(temp1*temp2)
                # print(sta)
            elif tokens[i]=='/':
                temp1=sta.pop()
                temp2=sta.pop()
                sta.append(int(temp2/temp1))
                # print(sta)
            else:
                sta.append(int(tokens[i]))
                # print(sta)
        # print(sta)
        return sta.pop()
                
                
                

        