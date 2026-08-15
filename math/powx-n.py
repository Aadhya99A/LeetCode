class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        #if x == 0:
         #   return 0
        return x*self.myPow(x, abs(n-1)) if n > 0 else x/(self.myPow(x, abs(n-1)))