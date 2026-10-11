class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        k = ""
        for i in digits:
            k += str(i)
        uk = str(int(k) + 1)
        return [int(j) for j in uk]
