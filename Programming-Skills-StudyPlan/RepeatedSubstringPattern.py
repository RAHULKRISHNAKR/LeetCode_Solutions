'''Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.'''


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for period in range(1, n // 2 + 1):
            if n % period == 0 and s[:period] * (n // period) == s:
                return True
        return False