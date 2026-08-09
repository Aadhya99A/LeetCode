import statistics as sts
class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        elv = []
        for num, freq in enumerate(count):
            elv += [num]*freq
        return [min(elv), max(elv), sts.mean(elv), sts.median(elv), sts.mode(elv)]
        