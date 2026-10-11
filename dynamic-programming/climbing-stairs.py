from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a+b
        return b