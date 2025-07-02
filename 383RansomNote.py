'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
'''

from collections import Counter as c

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r_count = c(ransomNote)
        m_count = c(magazine)

        for ch in r_count:
            if r_count[ch] > m_count.get(ch,0):
                return False
        return True