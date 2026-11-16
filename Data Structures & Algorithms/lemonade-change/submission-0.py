class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ini_set={5:0,10:0,20:0}
        for i in bills:
            if i==5:
                ini_set[5]+=1
            elif i==10:
                if ini_set[5]==0:
                    return False
                else:
                    ini_set[5]-=1
                    ini_set[10]+=1
            elif i==20:
                if ini_set[10]>0:
                    if ini_set[5]>0:
                        ini_set[5]-=1
                        ini_set[10]-=1
                        ini_set[20]+=1
                    else:
                        return False
                elif ini_set[5]>2:
                    ini_set[5]-=3
                    ini_set[20]+=1
                else:
                    return False
        return True
        



        