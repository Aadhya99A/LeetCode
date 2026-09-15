class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        ow = max(0, min(rec1[2],rec2[2]) - max(rec1[0],rec2[0]))
        oh = max(0, min(rec1[3],rec2[3]) - max(rec1[1],rec2[1]))

        return not oh*ow == 0