class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        dih = {int(i):0 for i in set(str(n))}
        for i in str(n):
            dih[int(i)] += 1
        k = 0
        for key, value in dih.items():
            k += key*value
        return k
