from collections import Counter
class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        digit_count = Counter(digits)
        valid_count = 0
        for num in range(100, 1000, 2):
            hundreds = num // 100
            tens = (num // 10) % 10
            units = num % 10
            req = Counter([hundreds, tens, units])
            if all(digit_count[d] >= req[d] for d in req):
                valid_count += 1
                
        return valid_count