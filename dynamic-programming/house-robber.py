class Solution:
    def rob(self, nums: List[int]) -> int:
        n1, n2 = 0, 0
        for i in nums[0::2]:
            n1 += i
        for j in nums[1::2]:
            n2 += j
        return max(n1, n2)