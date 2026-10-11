class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        sett = set(spaces)
        ret = ""
        i = 0
        while i < len(s):
            if i in sett:
                ret += " "
            
            ret += s[i]
            i += 1
        return ret