class Solution:
    def scoreOfString(self, s: str) -> int:
        ret = 0
        for i in range(len(s) -1 ):
            ret += abs(ord(s[i]) - ord(s[i+1]))
        return ret