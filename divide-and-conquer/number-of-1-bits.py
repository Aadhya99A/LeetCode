class Solution:
    def hammingWeight(self, n: int) -> int:
        k = 0
        for i in bin(n)[2:]:
            if i == "1":
                k += 1
        return k