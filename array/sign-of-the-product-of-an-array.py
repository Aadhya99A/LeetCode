class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = 0
        if 0 in nums:
            return 0
        else:
            for i in nums:
                if i < 0:
                    val += 1
            if val%2 == 0:
                return 1
            else:
                return -1