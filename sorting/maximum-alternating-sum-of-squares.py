class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        k = nums
        n = len(nums)
        for i in range(n):
            if k[i] < 0:
                k[i] = -k[i]
        k.sort()
        val = 0
        for j in range(n):
            if j < n//2:
                val -= (k[j])**2
            else:
                val += (k[j])**2
        return val