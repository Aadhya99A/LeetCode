from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        esl = Counter(nums)
        for key, value in esl.items():
            if value > 1:
                for k in range(value -1):
                    nums.remove(key)
        return len(nums)