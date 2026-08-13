class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        m = None
        while l <= r:
            m = l + (r - l)//2
            if x in range(m*m, (m+1)*(m+1)):
                return m
            elif m*m < x:
                l = m + 1
            elif m*m > x:
                r = m - 1