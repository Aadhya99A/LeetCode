class Solution:
    def countDigits(self, num: int) -> int:
        ret = 0
        for i in str(num):
            if num%(int(i)) == 0:
                ret += 1
        return ret