# Link on Task: https://leetcode.com/problems/palindrome-number/description/

# Solution

class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
        