class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:
        p_so = sorted(players)
        tr_so = sorted(trainers)

        c_lp = 0
        g_lp = 0

        matches = 0

        while g_lp < len(p_so) and c_lp < len(tr_so):
            if p_so[g_lp] <= tr_so[c_lp]:
                matches += 1
                c_lp += 1
                g_lp += 1
            else:
                c_lp += 1
        
        return matches