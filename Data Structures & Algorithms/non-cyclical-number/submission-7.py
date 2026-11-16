class Solution:
    def isHappy(self, n: int) -> bool:
        ini_sum=n
        seen_ele=set()
        while ini_sum!=1 and ini_sum not in seen_ele:
            seen_ele.add(ini_sum)
            ini_sum = sum(int(i)**2 for i in str(ini_sum))
            # print(ini_sum,seen_ele)
        # print(ini_sum,seen_ele)
        if ini_sum==1:
            return True
        else:
            return False
        
        