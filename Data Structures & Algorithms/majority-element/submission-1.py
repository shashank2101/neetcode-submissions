class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ini_ele=nums[0]
        c=1
        for i in range(1,len(nums)):
            if nums[i]==ini_ele:
                c+=1
            else:
                if c>0:
                    c-=1
                else:
                    ini_ele=nums[i]
        return ini_ele
                


        