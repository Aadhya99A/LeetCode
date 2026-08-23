class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        rp, lp = start, start
        while lp >= 0 or rp < len(nums):
            if rp < len(nums) and nums[rp] == target:
                return abs(rp - start)
            if lp >= 0 and nums[lp] == target:
                return abs(lp - start)
            lp -= 1
            rp += 1