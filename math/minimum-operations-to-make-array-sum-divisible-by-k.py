class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        m = sum(nums)
        return m%k