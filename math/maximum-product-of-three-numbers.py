class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        li = sorted(nums)
        n = len(li) - 1
        return max(li[n]*li[n-1]*li[n-2], li[n]*li[0]*li[1])
        