class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        elk = []
        sort_l = sorted(nums)
        for i in range(len(sort_l)):
            if sort_l[i]%k == 0:
                elk.append((sort_l[i])/k)
        for j in range(1, len(elk) + 2):
            if j not in elk:
                return k*j