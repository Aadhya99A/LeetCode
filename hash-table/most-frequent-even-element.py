class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        ek = {x:0 for x in set(sorted(nums))}
        for i in nums:
            ek[i] += 1
        if len(set(ek.values())) == 1:
            return -1
        mak = list(ek.values())[0]
        for key, value in ek.items():
            if value > mak:
                mak = value
        return mak