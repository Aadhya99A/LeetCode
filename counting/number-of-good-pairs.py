from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        checked = Counter(nums)
        there = 0
        for key, value in checked.items():
            if value > 1:
                there += value*(value-1)//2
        return there
        #here, combinations do the work
        #nC2 = n*(n-1)/2 