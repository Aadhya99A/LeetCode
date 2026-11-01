class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        std = sorted(nums)
        crm = 0
        lp, rp = 0, len(nums) -1
        while lp <= rp:
            nmax = std[lp]+std[rp]
            if nmax >= crm:
                crm = nmax
            lp += 1
            rp -= 1
        return crm