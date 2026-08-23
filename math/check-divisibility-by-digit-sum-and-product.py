class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sig = 0
        prod = 1
        for i in str(n):
            sig += int(i)
            prod = prod*(int(i))
        return n%(sig + prod) == 0