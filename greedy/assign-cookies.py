class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g_so = sorted(g)
        co_so = sorted(s)

        c_lp = 0
        g_lp = 0

        happy = 0

        while c_lp < len(s) and g_lp < len(g):
            if g_so[g_lp] <= co_so[c_lp]:
                happy += 1
                c_lp += 1
                g_lp += 1
            else:
                c_lp += 1
        
        return happy