class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = 0
        l1 = len(num1)
        n2 = 0
        l2 = len(num2)
        for i in range(l1):
            n1 += int(num1[i])*(10**(l1 - i - 1))
        for j in range(l2):
            n2 += int(num2[j])*(10**(l2 - j - 1))
        return str(n1*n2)