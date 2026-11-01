from itertools import combinations
class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        subsets = [[]]
        for element in nums:
            subsets += [current_sub + [element] for current_sub in subsets]
        return subsets