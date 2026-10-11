class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        emr = ""
        sm = sum([int(x) for x in str(n)])
        for i in str(n):
            if i != "0":
                emr += i
        return int(emr)* sm