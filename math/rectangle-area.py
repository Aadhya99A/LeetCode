class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        A1 = abs((ax1 - ax2)*(ay1 - ay2))
        A2 = abs((bx1 - bx2)*(by1 - by2))
        ow = max(0, min(ax2, bx2) - max(ax1, bx1))
        oh = max(0, min(ay2, by2) - max(ay1, by1))
        return A1 + A2 - oh*ow