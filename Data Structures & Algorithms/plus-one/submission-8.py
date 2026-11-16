class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        a="".join([str(i) for i in digits])
        a=int(a)+1

        return list(str(a))

        