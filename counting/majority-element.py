class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = None
        el = {x:nums.count(x) for x in set(nums)}
        if len(nums) % 2 == 0:
            for key, value in el.items():
                if value >= len(nums) / 2:
                    ret = key
        else:
            for key, value in el.items():
                if value >= len(nums) // 2 + 1:
                    ret = key
        return ret
