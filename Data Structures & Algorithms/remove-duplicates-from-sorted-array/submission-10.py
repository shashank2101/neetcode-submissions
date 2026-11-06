class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sample_set=set()
        last_ind=-1
        i=0
        while i<len(nums):
            if nums[i] in sample_set:
                i+=1
                continue
            else:
                sample_set.add(nums[i])
                last_ind+=1
                nums[last_ind]=nums[i]
                i+=1
            
        print(nums)
        return last_ind+1
            



             
        