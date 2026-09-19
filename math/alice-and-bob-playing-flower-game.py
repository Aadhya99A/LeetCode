class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m//2 * (n- n//2)) + ((m - m//2)*(n//2))
        #This has some big math behind it