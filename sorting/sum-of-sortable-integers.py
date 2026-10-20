class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        total = 0

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            ok = True
            for start in range(0, n, k):
                block = nums[start:start + k]
                end = start + k
                
                if sorted(block) != target[start:end]:
                    ok = False
                    break
                breaks = sum(block[i] > block[(i + 1) % k] for i in range(k))
                if breaks > 1:
                    ok = False
                    break

            if ok:
                total += k

        return total