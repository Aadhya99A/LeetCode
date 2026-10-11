from collections import Counter
class Solution:
    def maxDistinct(self, s: str) -> int:
        count = Counter(s)
        return len(count)