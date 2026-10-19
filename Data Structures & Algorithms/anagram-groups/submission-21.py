from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)  # Automatically creates an empty list for new keys
        for s in strs:
            key = ''.join(sorted(s))
            # print(ans,key)
            ans[key].append(s)
        return list(ans.values())
        