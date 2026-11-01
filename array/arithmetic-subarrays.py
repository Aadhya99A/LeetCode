class Solution:
    def isAP(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        lp, rp = 0, 1
        while rp < len(arr):
            if (arr[rp] - arr[lp]) != diff:
                return False
            lp += 1
            rp += 1
        return True 

    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        ret = []
        for i in range(len(l)):
            ret.append(self.isAP(nums[l[i]:(r[i]+1)]))
        return ret