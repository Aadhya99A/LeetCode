class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        if 1 in nums1:
            return True
        else:
            return all([i%2 == 0 for i in nums1])