class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r1 = [k for k in nums if k%2 == 0]
        r2 = [k for k in nums if k%2 != 0]
        return r1 + r2