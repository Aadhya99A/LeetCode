class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        n = 0
        ex = 0
        for num in nums:
            ex += num
            if ex == 0:
                n += 1
        return n