class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ret = None
        el = {x:0 for x in set(nums)}
        for i in nums:
            el[i] += 1
        if len(nums)%2 == 0:
            for key, value in el.items():
                if value >= len(nums)/2:
                    ret = key
        else:
            for key, value in el.items():
                if value >= len(nums)//2 + 1:
                    ret = key
        return ret