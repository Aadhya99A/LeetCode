class Solution:
    def maxProduct(self, n: int) -> int:
            k = [int(x) for x in str(n)]
            r = []
            for i in range(len(k)):
                for j in range(i+1, len(k)):
                    r.append(k[i]*k[j])
            return max(r)