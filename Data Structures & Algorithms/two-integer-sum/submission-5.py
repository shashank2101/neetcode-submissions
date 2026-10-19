class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a={}
        for i in range(len(nums)):
            res=target-nums[i]
            if res not in a.keys():
                a[nums[i]]=i
            elif res in a.keys():
                return [a[res],i]
        return []
        