class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ending_here=nums[0]
        max_so_far=nums[0]
        for i in (nums[1:]):
            max_ending_here=max(i,max_ending_here+i)
            max_so_far=max(max_ending_here,max_so_far)
        return max_so_far


        