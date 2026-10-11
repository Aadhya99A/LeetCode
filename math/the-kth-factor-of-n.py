class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        pf = sorted([x for x in range(1, n+1) if n%x ==0])
        if k >= len(pf) + 1:
            return -1
        else:
            return pf[k-1]