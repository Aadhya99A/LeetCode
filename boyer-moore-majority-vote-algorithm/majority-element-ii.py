from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counted = Counter(nums)
        ret = []
        for key in counted:
            if counted[key] > len(nums)//3:
                ret.append(key)
        return ret