class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        target = sum
        if target < 1 or target > 9 * num:
            return ""

        nines, remainder = divmod(target, 9)

        if remainder == 0:
            return "9" * nines + "0" * (num - nines)

        return "9" * nines + str(remainder) + "0" * (num - nines - 1)