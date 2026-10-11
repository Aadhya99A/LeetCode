class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, num in enumerate(nums):
            c = target - num
            if c in seen:
                return [seen[c], index]
            seen[num] = index


