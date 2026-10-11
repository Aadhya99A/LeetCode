class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1.extend(nums2)
        nums1.sort()
        for i in range(len(nums1) - m - n):
            nums1.remove(0)