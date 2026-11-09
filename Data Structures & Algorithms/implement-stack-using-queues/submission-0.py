from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        # Step 1: Push the new element into q2
        self.q2.append(x)
        
        # Step 2: Move all elements from q1 to q2
        while self.q1:
            self.q2.append(self.q1.popleft())
            
        # Step 3: Swap q1 and q2 so q1 always contains the stack elements
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        # The front of q1 is the top of the stack
        return self.q1.popleft()

    def top(self) -> int:
        # Look at the front of q1 without removing it
        return self.q1[0]

    def empty(self) -> bool:
        # Returns True if q1 is empty
        return not self.q1