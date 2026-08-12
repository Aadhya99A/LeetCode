class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        fq = {x:nums.count(x) for x in set(nums)}
        for key, val in fq.items():
            if val > k:
                fq[key] = k
        return sum(fq.values())