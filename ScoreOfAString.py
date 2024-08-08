'''
You are given a string s. The score of a string is defined as the sum of the absolute difference between the ASCII values of adjacent characters.

Return the score of s.
'''
class Solution:
    def scoreOfString(self, s: str) -> int:
        sumj=0
        i=1
        while i < len(s):
            sumj += abs(int(ord(s[i-1]))-int(ord(s[i])))
            i+=1
        return sumj
