class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        v1 = nums[:k] + nums[len(n) - k + 1]
        mappa = {x:0 for x in set(v1)}
        for i in v1:
            mappa[i] += 1
        if 1 in mappa.keys():
            return mappa.get(1)
        else:
            return -1
