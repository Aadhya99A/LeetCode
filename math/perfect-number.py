class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        el = [6, 28, 496, 8128, 33550336, 8589869056, 137438691328, 2305843008139952128]
        return num in el