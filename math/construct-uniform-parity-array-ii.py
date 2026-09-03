class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)
        has_odd = any(x % 2 != 0 for x in nums1)
        return mn % 2 != 0 or not has_odd