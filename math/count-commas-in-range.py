class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        if n >= 1000 and n < 10000:
            return n - 1000 + 1
        if n >= 10000 and n <= 100000:
            return n - 1000 + 1