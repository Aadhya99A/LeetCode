class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        a1 = []
        a2 = []
        cur1 = 0
        cur2 = 0
        for i in range(len(nums)):
            if i == 0:
                a1.append(nums[i])
                cur1 = nums[i]
            elif i == 1:
                a2.append(nums[i])
                cur2 = nums[i]
            elif cur1 > cur2:
                a1.append(nums[i])
                cur1= nums[i]
            else:
                a2.append(nums[i])
                cur2 = nums[i]
        return a1 + a2