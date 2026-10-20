from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        ing = "balon"
        counted = Counter(text)
        
        counted['o'] //= 2
        counted['l'] //= 2
        return min(counted[c] for c in ing)