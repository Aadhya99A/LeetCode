class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        v1 = nums.pop(nums.index(max(nums)))
        v2 = nums.pop(nums.index(max(nums)))
        return (v1 -1)*(v2 -1)