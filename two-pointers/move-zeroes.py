class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos] = nums[i]
                if insert_pos != i:
                    nums[i] = 0
                insert_pos += 1