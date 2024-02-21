# Link on Task: https://leetcode.com/problems/find-pivot-index/description/

# Solution

class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        isk_sum = sum(nums)
        left_sum = 0
        for i, value in enumerate(nums) :
            if left_sum * 2 == isk_sum - value:
                return i
            left_sum += value
        return -1
