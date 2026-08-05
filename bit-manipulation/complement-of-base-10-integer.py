class Solution:
    def bitwiseComplement(self, n: int) -> int:
        binl = bin(n)[2:]
        retx = "0b"
        for i in binl:
            if i == "1":
                retx += "0"
            elif i == "0":
                retx += "1"
        print (retx)
        return int(retx, 2)