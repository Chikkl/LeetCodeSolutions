# Link on Task: https://leetcode.com/problems/find-pivot-index/description/

# Solution

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
