class Solution:
    def reverse(self, x: int) -> int:
        if x not in range(-2**31 + 1, 2**31 - 1):
            return 0
        if x < 0:
            return -int(str(abs(x))[::-1])
        else:
            return int(str(x)[::-1])