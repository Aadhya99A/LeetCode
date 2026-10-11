from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        store = Counter(s1)
        lef, rig = 0, len(s1) -1
        anything = []
        while rig <= len(s2) -1:
            window = s2[lef:rig+1]
            if Counter(window) == store:
                return True
            else:
                lef += 1
                rig += 1
        return False