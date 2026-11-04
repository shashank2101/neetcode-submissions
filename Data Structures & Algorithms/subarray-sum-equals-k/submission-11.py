class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        pref_array=[0]*len(nums)
        ini_sum=0
        count=0
        for i in range(len(nums)):
            pref_array[i]=ini_sum+nums[i]
            ini_sum+=nums[i]
        print(pref_array)
        for i in range(len(nums)):
            if pref_array[i]-k in mp:
                count+=mp[pref_array[i]-k]
            mp[pref_array[i]]=mp.get(pref_array[i],0)+1
        print(mp)
        return count