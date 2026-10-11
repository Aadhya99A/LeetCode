class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ret = []
        for i in range(min(nums), max(nums)):
            if i not in nums:
                ret.append(i)
        return sorted(ret)