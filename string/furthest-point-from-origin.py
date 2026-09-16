from collections import Counter
class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cont = Counter(moves)
        return abs(cont["R"] - cont["L"]) + cont["_"]