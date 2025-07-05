'''Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.

Return the largest lucky integer in the array. If there is no lucky integer return -1.

 '''
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        from collections import Counter
        
        freq = Counter(arr)
        res=-1

        for n,c in freq.items():
            if n==c:
                res = max(res,n)
        return res