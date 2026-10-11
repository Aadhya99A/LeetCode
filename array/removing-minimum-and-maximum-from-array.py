class Solution:
    def minimumDeletions(self, nums: list[int]) -> int:
        indx = nums.index(max(nums))
        indn = nums.index(min(nums))
        evaln = [
    (max(indx, indn) + 1), 
    (len(nums) - min(indx, indn)), 
    (min(indx, indn) + 1 + len(nums) - max(indx, indn))
]
        return min(evaln)