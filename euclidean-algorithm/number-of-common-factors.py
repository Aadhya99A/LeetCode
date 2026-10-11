class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        return len({i for i in range(1, a+1) if a%i == 0} & {j for j in range(1, b+1) if b%j == 0})