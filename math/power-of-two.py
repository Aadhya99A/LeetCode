class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        for i in range(0, 32):
            if 2**i == n:
                return True
        return False