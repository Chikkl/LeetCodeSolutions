# Link on Task: https://leetcode.com/problems/roman-to-integer/description/

# Solution

class Solution(object):
    def romanToInt(self, s):
        roman_nums_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        list_with_num = list(s)
        result = 0
        for i in range(len(list_with_num)-1):
            if roman_nums_dict[list_with_num[i]] < roman_nums_dict[list_with_num[i+1]]:
                result -= roman_nums_dict[list_with_num[i]]
            else:
                result += roman_nums_dict[list_with_num[i]]
        return result+roman_nums_dict[list_with_num[-1]]
