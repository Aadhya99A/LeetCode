class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        A, B = 0, 0
        af = True
        while len(piles) != 0:
            if af:
                if piles[0] > piles[-1]:
                    A += piles.pop(0)
                elif piles [0] < piles[-1]:
                    A += piles.pop(-1)
                else:
                    A += piles.pop(-1)
                af = False
            else:
                if piles[0] > piles[-1]:
                    B += piles.pop(0)
                elif piles [0] < piles[-1]:
                    B += piles.pop(-1)
                else:
                    B += piles.pop(-1)
                af = True
        return A > B