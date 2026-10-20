class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        sumk = 0
        for num in nums:
            val = num%3
            if val == 2:
                sumk += 1
            else:
                sumk += val
        return sumk