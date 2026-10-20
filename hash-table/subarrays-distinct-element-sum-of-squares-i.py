class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            seen = set()
            dist = 0
            for j in range(i, n):
                if nums[j] not in seen:
                    seen.add(nums[j])
                    dist += 1
                ans += dist * dist

        return ans