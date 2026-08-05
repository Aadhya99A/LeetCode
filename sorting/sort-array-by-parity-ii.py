class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        ev = [k for k in nums if k%2 == 0]
        od = [k for k in nums if k%2 != 0]
        ret = []
        for index, num in enumerate(nums):
            if index%2 == 0:
                i = ev.pop()
                ret.append(i)
            elif index%2 != 0:
                j = od.pop()
                ret.append(j)
        return ret