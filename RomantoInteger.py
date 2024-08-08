'''
Given a roman numeral, convert it to an integer.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        prev_val = 0

        for char in s[::-1]:
            val = roman_map[char]
            if val < prev_val:
                total -= val
            else:
                total += val
            prev_val = val

        return total
