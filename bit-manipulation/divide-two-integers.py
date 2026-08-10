from math import floor, ceil
from math import copysign as sgn
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend//divisor > 2**31 - 1:
            return 2**31 - 1
        if dividend//divisor < -2**31:
            return -2**31
        if dividend/divisor > 0:
            return dividend//divisor
        else:
            return ceil(dividend/divisor)