class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        sta = []
        for i in asteroids:
            destroyed = False  # Flag to track if 'i' dies
            
            while sta and sta[-1] > 0 and i < 0:
                if abs(sta[-1]) < abs(i):
                    sta.pop()
                    continue
                elif abs(sta[-1]) == abs(i):
                    sta.pop()
                
                # If we get here, 'i' was destroyed
                destroyed = True
                break
            
            # If 'i' was never destroyed during the loop, append it
            if not destroyed:
                sta.append(i)
                
        return sta