class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ret = []
        psv = [i for i in nums if i > 0]
        neg = [j for j in nums if j < 0]
        pf = True
        for n in range(len(nums)):
            if pf:
                ret.append(psv[0])
                del psv[0]
                pf = False
            else:
                ret.append(neg[0])
                del neg[0]
                pf = True
        return ret