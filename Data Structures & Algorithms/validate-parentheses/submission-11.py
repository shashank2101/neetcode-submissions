class Solution:
    def isValid(self, s: str) -> bool:
        ope=['(','[','{']
        clo=[')',']','}']
        sta=[]
        for i in s:
            print(sta)
            if i in ope:
                sta.append(i)
            elif i in clo:
                if not sta:
                    return False
                temp1=sta[-1]
                temp2=i
                print(temp1,temp2,sta)
                if (temp1=='(' and temp2==')') or (temp1=='{' and temp2=='}') or (temp1=='[' and temp2==']'):
                    sta.pop()
                else:
                    return False
        if sta:
            return False
        return True

        