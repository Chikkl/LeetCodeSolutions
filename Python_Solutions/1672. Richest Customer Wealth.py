# Link on Task: https://leetcode.com/problems/richest-customer-wealth/description/

# Solution

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_each = 0
        for acc in accounts:
            if sum(acc) >= max_each:
                max_each = sum(acc)
        return max_each
