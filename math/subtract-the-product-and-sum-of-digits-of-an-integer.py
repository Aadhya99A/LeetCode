class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sumd = 0
        for dig in str(n):
            prod = prod*int(dig)
        for dig in str(n):
            sumd += int(dig)
        return prod - sumd