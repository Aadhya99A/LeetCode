class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        if target not in nums:
            return []
        k = nums
        k.sort()
        return [i for i in range(len(k)) if k[i] == target]