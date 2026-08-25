class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        valve = 1
        counted = 0
        for i in range(k):
            if max(happiness) > 0:
                valve += happiness.pop(happiness.index(max(happiness)))
                counted += 1
            else:
                break
        return valve - counted