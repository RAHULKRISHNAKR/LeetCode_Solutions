'''A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 '''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        List=set()
        for i in range(1,len(arr)):
            List.add(arr[i]-arr[i-1])
        if len(List)==1:
            return True
        return False