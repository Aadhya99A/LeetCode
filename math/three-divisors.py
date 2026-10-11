class Solution:
    def isThree(self, n: int) -> bool:
        return len([x for x in range(1, n+1) if n%x == 0]) == 3