class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        stables = []
        for i in range(len(nums)):
            inst = max(nums[:i+1]) - min(nums[i:])
            if inst <= k:
                stables.append(i)
        if stables:
            return min(stables)
        else:
            return -1