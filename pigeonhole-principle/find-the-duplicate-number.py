class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        snm = sorted(nums)
        old_curr = snm[0]
        new_curr = snm[1]
        for i in range(len(nums)):
            if i > 0:
                old_curr = snm[i-1]
                new_curr = snm[i]
            if new_curr == old_curr:
                return old_curr