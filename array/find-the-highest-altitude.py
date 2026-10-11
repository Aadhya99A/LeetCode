class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h = 0
        ret = []
        for i in gain:
            h += i
            ret.append(h)
        if max(ret) >= 0:
            return max(ret)
        else:
            return 0