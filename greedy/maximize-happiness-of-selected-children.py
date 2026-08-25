class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        valve = 1
        for i in range(k):
            if max(happiness) > 0:
                valve += happiness.pop(happiness.index(max(happiness)))
            else:
                break
        return valve - k