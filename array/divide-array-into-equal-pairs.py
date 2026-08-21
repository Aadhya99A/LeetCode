from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counted = Counter(nums)
        for i in counted.values():
            if i%2 != 0:
                return False
        return True