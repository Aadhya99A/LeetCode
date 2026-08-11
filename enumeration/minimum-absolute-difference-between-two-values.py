class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        if 1 not in nums or 2 not in nums:
            return -1
        k = []
        for i, item1 in enumerate(nums):
            for j, item2 in enumerate(nums):
                if item1 == 1 and item2 == 2:
                    k.append(abs(i -j))
        return min(k)