class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ret = 0
        for nk in range(1, n + 1):
            if nk%3 == 0 or nk%5 == 0 or nk%7 == 0:
                ret += nk
        return ret