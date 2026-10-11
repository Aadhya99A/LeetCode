class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        bk = 0
        for ind, num in enumerate(nums):
            ev = 0
            for j in str(num):
                ev += int(j)
            if ev == ind:
                return ind
        return -1