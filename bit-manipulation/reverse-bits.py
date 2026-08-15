class Solution:
    def reverseBits(self, n: int) -> int:
        s = bin(n)[2:]
        while len(s) < 32:
            s = "0" + s
        ret = ""
        for i in s[::-1]:
            ret += i
        return int("0b" + ret, 2)