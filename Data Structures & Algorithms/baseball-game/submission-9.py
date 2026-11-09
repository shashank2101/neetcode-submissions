class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sta = []
        for x in operations:
            if x == '+':
                # Sum of the previous two scores
                sta.append(sta[-1] + sta[-2])
            elif x == 'C':
                # Invalidate/remove the previous score
                sta.pop()
            elif x == 'D':
                # Double the previous score
                sta.append(2 * sta[-1])
            else:
                # Convert the number string to an integer and push it
                sta.append(int(x))
                
        return sum(sta)