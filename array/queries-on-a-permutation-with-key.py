class Solution:
    def processQueries(self, queries: list[int], m: int) -> list[int]:
        P = [i for i in range(1, m+1)]
        ret = []
        for i in queries:
            val = P.index(i)
            ink = P.pop(val)
            ret.append(val)
            P = [ink] + P
        return ret