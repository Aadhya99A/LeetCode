class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        lb, l = 0, 0
        rb, r = len(nums) - 1, len(nums) -1
        first = 0
        second = 0
        while lb <= rb:
            mid_1 = lb + (rb - lb)//2
            print("Loop 1:", mid_1)
            if target == nums[mid_1]:
                first = mid_1
                rb = mid_1 - 1
            elif target > nums[mid_1]:
                lb = mid_1 + 1
            elif target < nums[mid_1]:
                rb = mid_1 - 1
        print(first)
        while l <= r:
            mid_2 = l + (r - l)//2
            print("Loop 2:", mid_2)
            if l == r:
                break
            if target == nums[mid_2]:
                second = mid_2
                l = mid_2 + 1
            elif target > nums[mid_2]:
                l = mid_2 + 1
            elif target < nums[mid_2]:
                r = mid_2 - 1
        print(second)
        return [first, second]