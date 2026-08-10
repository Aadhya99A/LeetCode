class Solution:
    def reverse(self, x: int) -> int:
        k = None
        if x < 0:
            k = -int(str(abs(x))[::-1])
        else:
            k = int(str(x)[::-1])
        if k not in range(-2**31 + 1, 2**31 - 1):
            return 0
        else:
            return k