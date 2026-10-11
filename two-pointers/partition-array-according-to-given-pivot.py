class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        smalls = [i for i in nums if  i < pivot]
        bigs = [i for i in nums if  i > pivot]
        eqs = [pivot]*nums.count(pivot)
        return smalls + eqs + bigs