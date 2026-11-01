class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lp = 0
        rp = len(needle)
        while rp <= len(haystack):
            if haystack[lp:rp] == needle:
                return lp
            else:
                lp += 1
                rp += 1
        return -1