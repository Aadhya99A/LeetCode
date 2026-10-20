from collections import Counter
class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        emt = ""
        for num in nums:
            emt += str(num)
        if str(digit) in emt:
            counted = Counter(emt)
            return counted[str(digit)]
        else:
            return 0