'''Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).'''

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==0:
            low+=1
        if high%2==0:
            high-=1
        if low>high:
            return 0
        return (high-low)//2 + 1
        