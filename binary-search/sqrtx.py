class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        m = None
        while l <= r:
            m = l + (r - l)//2
            if x in range(m**2, (m+1)**2):
                return m
            elif m**2 < x:
                l = m + 1
            elif m**2 > x:
                r = m - 1